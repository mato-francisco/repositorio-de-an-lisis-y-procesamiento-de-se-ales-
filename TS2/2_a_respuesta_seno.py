


import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 


f=100
N=100
numero_periodos=3
fs=N*f/3

respuesta_impulso=np.zeros(N)


x=np.zeros(N)
x[0]=1

for n in np.arange(N):
    respuesta_impulso[n]=x[n]+3*x[n-10]


h=np.zeros(N)


t,x=funcion_sen(ff=f,nn=N,fs=fs)


for n in np.arange(N):
    h[n]=x[n]+3*x[n-10]

plt.figure(1)
plt.subplot(3,1,1)
plt.plot(np.arange(N),x,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal de entrada:senoidal de 100Khz")
plt.subplot(3,1,2)
plt.plot(np.arange(N),respuesta_impulso,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal respuesta al impulso")
plt.subplot(3,1,3)
plt.plot(np.arange(N),h,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal de salida del sistema")
plt.tight_layout() 
#-----------------------------------------------------por convolucion-------------------------


energia_entrada=np.sum(np.square(x)) 

energia_respuesta=np.sum(respuesta_impulso**2) 

E_N=(x/np.sqrt(energia_entrada))
     
RP_I=(respuesta_impulso/np.sqrt(energia_respuesta))



convolucio=np.convolve( E_N , RP_I ,mode="full")
plt.figure(2)
C_N=convolucio/np.sqrt(np.sum(np.abs(np.square(convolucio))))
print(np.sum(np.abs(np.square(C_N))))
plt.figure(2)
plt.subplot(3,1,1)
plt.plot(np.arange(N),x,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal de entrada:senoidal de 100Khz")
plt.subplot(3,1,2)
plt.plot(np.arange(N),respuesta_impulso,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal respuesta al impulso")
plt.subplot(3,1,3)
plt.plot(np.arange(2*N-1),C_N,linestyle='',marker='.' ,color='b')
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas')
plt.ylabel('eje de h[n]')
plt.title("señal de salida del sistema")
plt.tight_layout() 