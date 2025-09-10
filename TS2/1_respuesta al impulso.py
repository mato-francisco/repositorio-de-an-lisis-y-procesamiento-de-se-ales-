 
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 

N=100

h=np.zeros(N)

x=np.zeros(N)
x[0]=1
for n in np.arange(N):
    h[n]=3*(10**-2)*x[n]+5*(10**-2)*x[n-1]+3*(10**-2)*x[n-2]+1.5*h[n-1]-0.5*h[n-2]
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