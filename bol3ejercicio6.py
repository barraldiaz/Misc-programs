
'''Angel Barral Diaz'''

from numpy import*
from matplotlib.pyplot import*



#Seleccionamos los parametros:

N=20; dimt=1000
deltat=0.1;deltax=0.5;u=1;alfa=1
s=alfa*deltat/deltax**2
c=u*deltat/deltax
T=zeros(N+1)
Tnew=zeros(N+1)

#Condiciones iniciales:
T[:]=0
T[2:5]=2

figure(1);plot(T,color='royalblue');pause(0.1)

for i in range(dimt):
    
    #Condiciones de frontera:
    T[0]=0
    T[N]=0
    
    
    for i in range(1,N):
        Tnew[i]=T[i]+s*(T[i-1]-2*T[i]+T[i+1])-c/2*(T[i+1]-T[i-1])
    
    Tnew[N]=0
    Tnew[0]=0
    #Actualizamos las variables:
    for i in range(0,N+1):
        T[i]=Tnew[i]
    
    #Ploteamos cada 10 N:
        
    if N%10==0:
        figure(1)
        plot(T)
        pause(0.01)    
        show
        
    
xlabel=('i-inidce')
ylabel=('temp')
