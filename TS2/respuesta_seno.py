
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(ff,nn,vmax=1,dc=0,ph=0,fs=2):#todas las variables que estan igualadas a un valor seran las 
                                             #opcionale y si nos las pongo cuando llamo la funcion toma esos 
                                             #valore. fs = 2 para que cumpla nyquis 
    
    t=np.arange(0,(nn)/fs,1/fs)
   
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t,y 
f=2000
N=1000
numero_periodos=3
fs=N*f/numero_periodos

h=np.zeros(N)
h_100=np.zeros(100)

t , x = funcion_sen(ff=2000,nn=N,fs=fs)
t , x_100 = funcion_sen(ff=2000,nn=100,fs=fs)

for n in np.arange(N):
    h[n]=3*(10**-2)*x[n]+5*(10**-2)*x[n-1]+3*(10**-2)*x[n-2]+1.5*h[n-1]-0.5*h[n-2]
for n in np.arange(100):
    h_100[n]=3*(10**-2)*x_100[n]+5*(10**-2)*x_100[n-1]+3*(10**-2)*x_100[n-2]+1.5*h_100[n-1]-0.5*h_100[n-2]
plt.figure(1)
plt.plot(np.arange(N),(h), label="respuesta al impulso",linestyle='-',marker='.' ,color='b')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas)')
plt.ylabel('eje de h[n]')
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()
fft=np.fft.fft(h)

ffabs=np.abs(fft)

plt.figure(2)
plt.plot(np.arange(N),(ffabs), label="respuesta al impulso",linestyle='-',marker='.' ,color='b')
plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('eje de n muestras discretas)')
plt.ylabel('eje de h[n]')
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout()