
'''Angel Barral Diaz'''




from numpy import*
from matplotlib.pyplot import*


#we select the parameters:

N=10 ; dimt=500
deltat=0.1;deltax=1;deltay=1
alfax,alfay=1,1
sx=alfax*deltat/deltax/deltax
sy=alfay*deltat/deltay/deltay

T=zeros((N+1,N+1))
Tnew=zeros((N+1,N+1))

#Initial conditions:
T[:,:]=0

figure(1)

#Frontier conditions:
#T[1,48:53]=400

#T[45:55,45:55]=100
T[1:8,7:13]=50

for n in range(dimt):
    for i in range(1,N):
        for j in range(1,N):
            Tnew[i,j]=T[i,j]+sx*(T[i-1,j]-2*T[i,j]+T[i+1,j])+sy*(T[i,j-1]-2*T[i,j]+T[i,j+1])
    for i in range(N+1):
        Tnew[i,0]=0
        Tnew[i,N]=0
    for j in range(N+1):
        Tnew[0,j]=0
        Tnew[N,j]=0
    for i in range(0,N+1):
        for j in range(N+1):
            T[i,j]=Tnew[i,j]
 
    if n%1==0:
        imshow(T,cmap='hot',vmin=0,vmax=50,interpolation='gaussian')
        pause(0.001)
