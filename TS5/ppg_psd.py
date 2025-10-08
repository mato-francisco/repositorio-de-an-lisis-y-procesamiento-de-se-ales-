import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write
import sounddevice as sd


fs_ppg = 400 # Hz

ppg = np.load('ppg_sin_ruido.npy')

plt.figure(1)
plt.plot(ppg)

promedios=5
zero_padding=2
nperseg=ppg.shape[0]//promedios

f_welch_ppg , psd_welch_ppg = sig.welch(x=ppg, fs=fs_ppg ,window="hamming",nperseg = nperseg, nfft=zero_padding*nperseg)

area=np.cumsum(psd_welch_ppg)

bb_max=np.where((area/np.max(area))>0.99)
bw_max=f_welch_ppg [bb_max[0][0]]

#fijarte minimo es agarra el maximo del ancho de banda y cortar en el punt0
#de frecuencia 

bb_min=np.where(psd_welch_ppg>psd_welch_ppg[bb_max[0][0]])
bw_min=f_welch_ppg[bb_min[0][0]]


plt.figure(2)
plt.plot(f_welch_ppg,psd_welch_ppg,label="hamming")
plt.axvline(x=bw_max,color='r')
plt.axvline(x=bw_min,color="r")
plt.xlim(0,7)

