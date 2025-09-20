import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft

nn=1000
fs=nn
deltaf=fs/nn


t=np.arange(-10,10,0.1)

x=np.abs(np.sin(np.pi*t)/(np.sin(np.pi*t/nn))*nn)
plt.plot(t,x) 

plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('f(w)')

#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()