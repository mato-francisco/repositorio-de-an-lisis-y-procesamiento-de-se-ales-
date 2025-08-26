import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sp

def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 


ff=2000
ph=0
vmax=1
dc=0
nn=25*2
fs=50000
#ejemplo de clase: se quiere ver la señal  en 1s por lo tanto la relación queda N = ts
#para ver tantas muestras en un periodo, hay que hacer "periodo/muestras=periodo de muestro"

tiempo_a , espacio_a = funcion_sen(vmax,dc,ff,ph,nn,fs)

tiempo_b , espacio_b = funcion_sen(np.pi/2,dc,ff/2,np.pi/2,nn,fs)

plt.figure(1)
plt.subplot(2,1,1)
plt.plot(tiempo_a,espacio_a,label=("N=",nn,"fs=",fs) ,linestyle='-' ,color='r')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')

plt.subplot(2,1,2)
plt.plot(tiempo_b,espacio_b,label=("N=",nn,"fs=",fs), linestyle='-' ,color='g')
plt.legend()

plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) #en donde aparece el cuadro

plt.tight_layout()
plt.draw()

#------------------------modulada

# tiempo_c , espacio_c = funcion_sen(vmax,dc,ff/2,ph,nn,fs)

# espacio_ac=espacio_a *espacio_c

# plt.figure(2)

# plt.plot(tiempo_a,espacio_a, linestyle='-' ,color='r')
# plt.plot(tiempo_b,espacio_c, linestyle='-' ,color='g')
# plt.plot(tiempo_a,espacio_ac, linestyle='-' ,color='b')

# plt.grid(True, linestyle=':') 
# plt.xlabel('Eje X')
# plt.ylabel('Eje Y')
# plt.title('N=',nn,"fs=",fs)
# plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) #en donde aparece el cuadro
# plt.draw()

#------------------------potencia

recortada=np.clip(espacio_a,-0.375,0.375)

plt.figure(3)

plt.plot(tiempo_a,espacio_a, linestyle='-.' ,color='r')

plt.plot(tiempo_a,recortada, linestyle='-.' ,color='b')


plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([np.min(tiempo_b),np.max(tiempo_b),-2,2]) 

plt.draw()

#-------------------------------cuadrada

t=np.linspace(0,1,500)
espacio_cuadrado=sp.square(2 * np.pi * 2000 * t)

plt.figure(4)

plt.plot(t,espacio_cuadrado, linestyle='-' ,color='b')


plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.axis([0,1,-2,2]) 

#-------------------------------
plt.show()

