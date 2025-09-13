import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft
from scipy import signal
from scipy.fft import fft, fftshift


N=1000
fs=N
deltaf=fs/N
a_0=np.sqrt(2)
snr_db=1

#---------------------------------------------
# rea_blakman=np.zeros(200)

# for j in np.arange(200):
#     omega_0=fs/4
    
#     fr=np.random.uniform(-2,2)
#     omega_1=omega_0+fr*deltaf
#     rea_blakman[j]=omega_1
#---------------------------------------------
# rea_rectangular=np.zeros(200)

# for j in np.arange(200):
#     omega_0=fs/4
    
#     fr=np.random.uniform(-2,2)
#     omega_1=omega_0+fr*deltaf
#     rea_rectangular[j]=omega_1

#---------------------------------------------
# rea_flattop=np.zeros(200)
# for j in np.arange(200):
#     omega_0=fs/4
    
#     fr=np.random.uniform(-2,2)
#     omega_1=omega_0+fr*deltaf
#     rea_flattop[j]=omega_1
#---------------------------------------------
# rea_kaiser=np.zeros(200)
# for j in np.arange(200):
#      omega_0=fs/4
#      fr=np.random.uniform(-2,2)
#      omega_1=omega_0+fr*deltaf
#      rea_kaiser[j]=omega_1   

#matrix = np.array([rea_flattop, rea_blakman,rea_kaiser,rea_rectangular])



omega_0=fs/4    
fr=np.random.uniform(-2,2)
fr=0
omega_1=omega_0+fr*2*deltaf

dev_estandar=np.sqrt(10**(-(snr_db-10*np.log10(((a_0)**2)/2))/10))


n=np.arange(0,N/fs,1/fs )

s_1=a_0*np.sin(omega_1*n)

ruido=np.random.normal(0,dev_estandar,N)

x_1=s_1+ruido
#señal modificada = señal + ruido

#sin fr, snr chequear, y ventaneado rectangular con un solo fr chaquear

ffsen=(1/N)*np.fft.fft(x_1)



plt.figure(1)


plt.plot(np.arange(N)*deltaf,10*np.log10((np.abs(ffsen)**2)),linestyle='',marker='x' ,color='r',)
plt.grid(True, linestyle=':') 
plt.xlabel('frecuencia (HZ)')
plt.ylabel('f(w)')
plt.xlim(0,N/2)
#plt.axis([0,nn/2,0,10000]
plt.draw()
plt.tight_layout()


