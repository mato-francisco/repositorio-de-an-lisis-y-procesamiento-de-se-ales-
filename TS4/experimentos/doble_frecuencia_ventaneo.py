import numpy as np
from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt

N=1000
fs=N
deltaf=fs/N
a_0=2
snr_db=3
realizaciones=200
   
hamming = signal.windows.hamming(N)

flatop = signal.windows.flattop(N)


blackmanharris = signal.windows.blackmanharris(N)






omega_1=N/4

t=np.arange(0,(N)/fs,1/fs)


x_1=np.sin(omega_1*2*np.pi*t)+np.sin((omega_1+0.7)*2*np.pi*t)



zero_padding=10


ffx_1=(1/(N))*np.fft.fft(x_1,n=zero_padding*N,axis=0)
absffx_1=np.abs(ffx_1)
ff=np.arange(zero_padding*N)*(fs/(zero_padding*N))

ffx_2=(1/(N))*np.fft.fft(x_1*hamming,n=zero_padding*N,axis=0)
absffx_2=np.abs(ffx_2)
ff=np.arange(zero_padding*N)*(fs/(zero_padding*N))

ffx_3=(1/(N))*np.fft.fft(x_1*flatop,n=zero_padding*N,axis=0)
absffx_3=np.abs(ffx_3)
ff=np.arange(zero_padding*N)*(fs/(zero_padding*N))

ffx_4=(1/(N))*np.fft.fft(x_1*blackmanharris,n=zero_padding*N,axis=0)
absffx_4=np.abs(ffx_4)
ff=np.arange(zero_padding*N)*(fs/(zero_padding*N))



plt.plot(ff,absffx_1,linestyle='',marker='X' ,color='b',label='rec')
plt.plot(ff,absffx_2,linestyle='',marker='X' ,color='r',label='ham')
plt.plot(ff,absffx_3,linestyle='',marker='X' ,color='g',label='fla')
plt.plot(ff,absffx_4,linestyle='',marker='X' ,color='c',label='bla')

plt.legend()
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('amplitud[db]')
plt.xlim(240,260)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout() 

plt.show()