 
import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
def funcion_sen(vmax,dc,ff,ph,nn,fs):
    
    t=np.arange(0,(nn)/fs,1/fs)
    
    y=vmax*np.sin(ff*2*np.pi*t-ph)+dc
    
    return t ,y 
nn=1000
fs=nn
deltaf=fs/nn
x , y =funcion_sen(1, 0, deltaf*(nn/4) ,0 ,nn ,fs )
x , z =funcion_sen(1, 0,deltaf*(nn+1)/4 ,0 ,nn ,fs )
x , w =funcion_sen(1, 0, deltaf*((nn+0.5)/4 ),0 ,nn ,fs )
        
ffty=np.fft.fft(y)
fftz=np.fft.fft(z)
fftw=np.fft.fft(w)

plt.figure(1)

plt.plot(np.arange(0,nn/1),np.abs(ffty), linestyle='',marker='.' ,color='b')
plt.plot(np.arange(0,nn/1),np.abs(fftz), linestyle='',marker='.' ,color='g')
plt.plot(np.arange(0,nn/1),np.abs(fftw), linestyle='',marker='.' ,color='r')
plt.grid(True, linestyle=':') 
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 
plt.show()