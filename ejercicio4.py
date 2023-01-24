# -*- coding: utf-8 -*-
'''Angel Barral Diaz'''

from numpy import*
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#Numero de iteraciones:

n=5000

#Introducimos las constantes y valores iniciales:

a,b,d=1,0.1,0.1
dt=0.01

#Definimos las funciones a integrar:

def dv(u,v):
    dv=b*v*(1-v/u)
    return dv
def du(u,v):
    du=u*(1-u)-(a*u*v)/(u+d)
    return du
#==========================================================================================================
#Metodo de Runge-Kuta de 4o orden:

u,v,t=0.1,0.5,0
U=[u]
V=[v]
T=[t]
for i in range(n):
    t=t+dt
    kx1=dt*du(u,v)
    ky1=dt*dy(x,y,z)
  

    kx2=dt*dx(x+kx1/2,y+ky1/2)
    ky2=dt*dy(x+kx1,y+ky1,z+kz1/2)

    
    kx3=dt*dx(x+kx2/2,y+ky2/2)
    ky3=dt*dy(x+kx2,y+ky2,z+kz2/2)
 
    
    kx4=dt*dx(x+kx3/2,y+ky3/2)
    ky4=dt*dy(x+kx3,y+ky3,z+kz3/2)

    
    
    u=u+ku1/6.+ku2/3.+ku3/3.+kx4/6.
    y=y+ky1/6.+ky2/3.+ky3/3.+ky4/6.

    
    V.append(v)
    U.append(u)
    T.append(t)

#==========================================================================================================
#Ploteamos los datos:
#3D
fig=plt.figure(figsize=(6,6))
ax=fig.add_subplot(111,projection='3d')
ax.set_xlabel('eje X')
ax.set_ylabel('eje Y')
ax.set_zlabel('eje Z')
ax.set_title('Metodo Runge Kutta orden 4, dt=0.01')
ax.scatter(X,Y,Z,color='darkgreen',marker='>',s=12)

#Ejes separados
figure, axes = plt.subplots(nrows=2, ncols=2)
figure.suptitle('Metodo Runge-Kutta orden 4', fontsize=12)
axes[0,0].plot(T,X,'.',ms=2, color='k',label='X')
axes[0,0].legend(loc='best')
axes[0,0].set_ylabel('X')
axes[0,1].plot(T,Y,'.',ms=2,color='brown',label='Y')
axes[0,1].legend(loc='best')
axes[1,0].plot(T,Z,'.',ms=2,color='darkgreen',label='Z')
axes[1,0].set_xlabel('tiempo t')
axes[1,0].set_ylabel('Z')
axes[1,0].legend(loc='best')
axes[1,1].plot(T,X,'.',ms=1,color='k')
axes[1,1].plot(T,Y,'.',ms=1,color='brown')
axes[1,1].plot(T,Z,'.',ms=1,color='darkgreen')
axes[1,1].set_xlabel('tiempo t')
plt.show()

