import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write
import sounddevice as sd

fs_audio, wav_data = sio.wavfile.read('silbido.wav')

plt.figure(1)
plt.plot(wav_data)

#---------------------------welch------------------------------------
promedios=200
zero_padding=2
nperseg=wav_data.shape[0]//promedios

f_welch_ha , psd_welch_ha=sig.welch(x=wav_data, fs=fs_audio ,window="hamming",nperseg = nperseg, nfft=zero_padding*nperseg)

area=np.cumsum(psd_welch_ha)
bb_max=np.where((area/np.max(area))>0.99)
bw_max_welch=f_welch_ha[bb_max[0][0]]

bb_min=np.where(psd_welch_ha>psd_welch_ha[bb_max[0][0]])
bw_min_welch=f_welch_ha[bb_min[0][0]]

plt.figure(2)
plt.plot(f_welch_ha,psd_welch_ha)
plt.xlabel("eje de frecuencias discretas")
plt.ylabel("eje de densidad espectral de potencia")
plt.title("welch")
plt.axvline(x=bw_max_welch,color='r')
plt.axvline(x=bw_min_welch,color="r")
plt.xlim(0,10000)

#----------------------periodograma modificado-------------
#aclaracion: por se que lo tranformamos medio a mano las frecuencias se repite en nyquist por lo tanto 
#hay que cortar a la mitad la dessidad espectral de potencia
hamming = sig.windows.hamming(len(wav_data))

x_n=hamming*wav_data
dsp_perio=np.fft.fft(x_n)
dsp_perio=(np.abs(dsp_perio)**2)/len(wav_data)
dsp_perio=dsp_perio[0:72000]
f_perio=(fs_audio/len(wav_data))*np.arange(len(dsp_perio))

area=np.cumsum(dsp_perio)

bb_max=np.where((area/np.max(area))>0.99)
bw_max_perio=f_perio[bb_max[0][0]]

bb_min=np.where(dsp_perio>=dsp_perio[bb_max[0][0]])
bw_min_perio=f_perio[bb_min[0][3]]


plt.figure(3)
plt.plot(f_perio,dsp_perio)
plt.xlabel("eje de frecuencias discretas")
plt.ylabel("eje de densidad espectral de potencia")
plt.title("periodograma modificado")
plt.axvline(x=bw_max_perio,color='r')
plt.axvline(x=bw_min_perio,color="r")