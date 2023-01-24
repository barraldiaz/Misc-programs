# -*- coding: utf-8 -*-

'''Angel Barral Diaz'''

import numpy as np
import matplotlib.pyplot as plt

#Numero de iteraciones:
n=400

#Definimos las condiciones iniciales

dti=0.01
deltat=dti
r=1
k=1
t,P=1,10

Paux=P
#Limites superior e inferior para la diferencia de P(n)-P(n-1):
sup=0.1
inf=1e-2
diff=sup+1

#Vectores de datos:

P4=[P]
T=[t]
deltats=[deltat]

#====================================================================================================
#Metodo de Runge-kutta de orden 4:

for i in range(n):
    print(i)
    
    while diff<inf or diff>sup:
        
        t=t+deltat
        k1=deltat*r*P*(1-P/k)
        k2=deltat*r*(P+k1/2)*(1-(P+k1/2)/k)
        k3=deltat*r*(P+k2/2)*(1-(P+k2/2)/k)
        k4=deltat*r*(P+k3/2)*(1-(P+k3/2)/k)
        
        Pnew=P+k1/6+k2/3+k3/3+k4/6
        P=Pnew
        t=t-deltat
        diff=abs(Pnew-Paux)
        Paux=Pnew
        
        print(deltat)
        if diff<inf:
            deltat=deltat+deltat/10
            print('aum')
            
        if diff>sup:
            deltat=deltat-deltat/2
            print('dism')
        if deltat>dti*1e10:
            deltat=deltat*1e-10
            break
            print('disdel')
        if diff<dti*1e-10:
            deltat=deltat*1e-10
            print('aumdelt')
            break
        
    P=Paux
    t=t+deltat
    k1=deltat*r*P*(1-P/k)
    k2=deltat*r*(P+k1/2)*(1-(P+k1/2)/k)
    k3=deltat*r*(P+k2/2)*(1-(P+k2/2)/k)
    k4=deltat*r*(P+k3/2)*(1-(P+k3/2)/k)
            
    Pnew=P+k1/6+k2/3+k3/3+k4/6
    P=Pnew
    diff=abs(Pnew-Paux)
    print(diff)
    Paux=Pnew
        
    P4.append(P)
    T.append(t)
    deltats.append(deltat)

    
#====================================================================================================
#Ahora ploteamos la funcion obtenida:


plt.plot(T,P4,'-',color='darkgreen',ms=4,label='Runnge-Kutta orden 4')
plt.legend(loc='best')
plt.ylabel('Poblacion P')
plt.xlabel('tiempo t')
plt.show()


#Grafica con la variacion de deltat:
'''
plt.plot(range(n+1),deltats,'-',color='darkgreen',ms=4,label='Evolución de dt')
plt.show()
plt.legend(loc='best')
plt.ylabel('Delta t')
plt.xlabel('iteracion i')
plt.show()
'''