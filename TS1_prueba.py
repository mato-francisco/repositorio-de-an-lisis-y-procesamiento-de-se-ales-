import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sp
from scipy.fft import fft, fftshift
ff=2000
periodos_visible=3
N=1000
fs=N*ff/periodos_visible
deltaf=fs/N

t=np.arange(0,(N)/fs,1/fs)

seno=np.sin(ff*2*np.pi*t)

des_seno=(np.pi/2)*np.sin(ff*2*np.pi*t+np.pi/2)

modulado_seno=np.sin(ff*2*np.pi*t)*np.sin((ff/2)*2*np.pi*t)

potencia=(1/(N))*np.sum(np.abs(seno)**2)*0.75

recortada=np.clip(seno,-potencia,potencia)


cuadrada= sp.square(2 * np.pi * 5 * t)

pulso=np.zeros(N,dtype=float)
for k in np.arange(0,N):
    if(t[k]<0.01):
        
        pulso[k]=1
    else:
        pulso[k]=0

plt.figure(1)

plt.plot(t,seno,linestyle='',marker=".")

aux=np.abs(np.fft.fft(seno))
aux_1=aux[2000]

plt.grid(True, linestyle=':') 
plt.tight_layout() 
plt.xlabel('eje de muestras n')
plt.ylabel('eje de amplitud')

plt.draw()
plt.show
