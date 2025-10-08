
import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write
import sounddevice as sd

ecg_one_lead = np.load('ecg_sin_ruido.npy')
fs_ecg = 1000 # Hz

promedios=10
zero_padding=2
nperseg=ecg_one_lead.shape[0]//promedios

f_welch , psd_welch=sig.welch(x=ecg_one_lead, fs=fs_ecg ,window="hamming",nperseg = nperseg, nfft=zero_padding*nperseg)


area=np.cumsum(psd_welch)

bb_max=np.where((area/np.max(area))>0.99)
bw_max=f_welch [bb_max[0][0]]

#fijarte minimo es agarra el maximo del ancho de banda y cortar en el punt0
#de frecuencia 

bb_min=np.where(psd_welch>psd_welch[bb_max[0][0]])
bw_min=f_welch [bb_min[0][0]]


plt.figure(3)
plt.plot(f_welch ,psd_welch,label="hamming")
plt.axvline(x=bw_max,color='r')
plt.axvline(x=bw_min,color="r")

plt.xlim(0,50)