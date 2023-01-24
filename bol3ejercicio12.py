'''Angel Barral Diaz'''

from numpy import*
from matplotlib.pyplot import*
from numpy.linalg import inv

Nx=20;Ny=20; dimt=500
deltat=0.1;deltax=1;deltay=1
figure(1)
alfax,alfay=1,1
sx=alfax*deltat/deltax/deltax
sy=alfay*deltat/deltay/deltay

T=zeros((Ny+1,Nx+1))

Tnew=copy(T)

for t in range(dimt):
    for i in range(0,Ny):
        for j in range(0,Nx):
            Tnew[i,j]=T[i,j]+sy*(T[i-1,j]-2*T[i,j]+T[i+1,j])+sx*(T[i,j-1]-2*T[i,j]+T[i,j+1])
    
    T=copy(Tnew)
    T[0,:]=50
    T[-1,:]=30
    #T[int(Ny/2),:]=50*abs(sin(0.01*t))
    if t%10==0:
        imshow(T,vmin=0,vmax=50,cmap='hot',interpolation='bilinear')
        pause(0.01)
        
            

