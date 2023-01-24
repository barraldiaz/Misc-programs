


'''Angel Barral Diaz'''

from numpy import*
from matplotlib.pyplot import*
from numpy.linalg import inv

N=20; dimt=3000
deltat=0.01;deltax=0.5;u=1
figure(1)

c=u*deltat/deltax

T=zeros(N+1)
Tnew=zeros(N+1)
Tnew=vstack(Tnew)
T=vstack(T)

#Condicion inicial:
T[1]=5
#Condicion de contorno:
T[0]=0
T[-1]=0

B=zeros((N+1,N+1))
for i in range(N):
    B[i,i]=1
for i in range(N):
    B[i+1,i]=c/4
    B[i,i+1]=-c/4
B[0,1]=0
B[-1,-2]=0
B[0,0]=1
B[-1,-1]=1


A=zeros((N+1,N+1))
for i in range(N):
    A[i,i]=1
for i in range(N):
    A[i+1,i]=-c/4
    A[i,i+1]=+c/4
A[0,1]=0
A[-1,-2]=0
A[0,0]=1
A[-1,-1]=1

for n in range(dimt):
    T[0]=0
    T[-1]=0
    invA=inv(A)
    
    Tnew=invA.dot(B.dot(T))
    Tnew[0]=0
    Tnew[-1]=0
    T=Tnew
    
    pause(0.01)
    
    plot(T, color='b')
    plt.figure(1)
    show
