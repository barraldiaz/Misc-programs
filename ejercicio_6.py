# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 16:24:02 2020

@author: nacho
"""
from numpy import *
import matplotlib.pyplot as plt
from numpy import random as rd


N=5 ; dimt=2000
dt=0.01 ; dx=0.5 ; a=1
s=a*dt/dx**2
####################FCTS IMPLICITO####################
T=zeros(N+1)
T=vstack(T)
Tnew=zeros(N+1)
Tnew=vstack(Tnew)

A=zeros((N+1,N+1))

for i in range(0,N+1):
    for j in range(0,N+1):
        if i==j and i!=0 and i!=N:
            A[i,j]=1+s
        if j==i+1:
            A[i,j]=-s/2
        if j==i-1:
            A[i,j]=-s/2
A[0,0],A[-1,-1]=1,1
A[0,1],A[-1,-2]=0,0

B=zeros((N+1,N+1))
for i in range(0,N+1):
    for j in range(0,N+1):
        if i==j and i!=0 and i!=N:
            B[i,j]=1-s
        if j==i+1:
            B[i,j]=s/2
        if j==i-1:
            B[i,j]=s/2
B[0,0],B[-1,-1]=1,1
B[0,1],B[-1,-2]=0,0

#Condiciones de frontera    
T[0]=10
T[-1]=5
Ai=linalg.inv(A) 
#Condiciones iniciales

for i in reversed(range(len(T))):
    T[i]=sin(0.3*i)**2*10

T[0]=0
T[-1]=5

plt.clf()
plt.plot(T)
plt.pause(3)
for n in range(dimt):
    Tnew=Ai.dot(B.dot(T))
    T=Tnew
    T[0]=0
    T[-1]=5
    if n%50==0:         #dibujamos
        plt.figure(1)
        plt.pause(0.1)
        plt.plot(T)
        plt.show()  