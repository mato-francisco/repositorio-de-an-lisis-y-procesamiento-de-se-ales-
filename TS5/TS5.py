import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write
import sounddevice as sd

# ecg_one_lead = np.load('ecg_sin_ruido.npy')
# fs_ecg = 1000 # Hz


# promedios=60
# zero_padding=10
# nperseg=ecg_one_lead.shape[0]//promedios

# f_welch , dsd_welch=sig.welch(x=ecg_one_lead, fs=fs_ecg ,window="hamming",nperseg = nperseg,nfft=zero_padding*ecg_one_lead.shape[0])


# plt.figure(1)
# plt.plot(ecg_one_lead)

# plt.figure(2)

# plt.plot(f_welch,10*np.log10(np.abs(dsd_welch)**2))

# plt.xlim(0,200)


fs_audio, wav_data = sio.wavfile.read('silbido.wav')

plt.figure(1)
plt.plot(wav_data)

promedios=10
zero_padding=2
nperseg=wav_data.shape[0]//promedios

# f_welch_bo , psd_welch_bo=sig.welch(x=wav_data, fs=fs_audio ,window="bohman",nperseg = nperseg,nfft=zero_padding*nperseg)
#---------------------------
f_welch_ha , psd_welch_ha=sig.welch(x=wav_data, fs=fs_audio ,window="hamming",nperseg = nperseg,nfft=zero_padding*nperseg)
#--------------------------
# f_welch_tu , psd_welch_tu=sig.welch(x=wav_data, fs=fs_audio ,window="tukey",nperseg = nperseg,nfft=zero_padding*nperseg)
# f_welch_fl , psd_welch_fl=sig.welch(x=wav_data, fs=fs_audio ,window="flattop",nperseg = nperseg,nfft=zero_padding*nperseg)
# f_welch_bh , psd_welch_bh=sig.welch(x=wav_data, fs=fs_audio ,window="blackmanharris",nperseg = nperseg,nfft=zero_padding*nperseg)
# f_welch_ta , psd_welch_ta=sig.welch(x=wav_data, fs=fs_audio ,window="taylor",nperseg = nperseg,nfft=zero_padding*nperseg)


# plt.plot(f_welch_bo,psd_welch_bo,label="bohman")
#------------------------------------------------------

#------------------------------------------------------
# plt.plot(f_welch_tu,psd_welch_tu,label="tukey")
# plt.plot(f_welch_fl,psd_welch_fl,label="flattop")
# plt.plot(f_welch_bh,psd_welch_bh,label="blackmanharris")
# plt.plot(f_welch_ta,psd_welch_ta,label="taylor")



#a medida que el ancho del lobulo principal de la ventana crece,disminuye  la resolucucion 

area=np.cumsum(psd_welch_ha)

bb_max=np.where((area/np.max(area))>0.99)
bw_max=f_welch_ha[bb_max[0][0]]

#fijarte minimo es agarra el maximo del ancho de banda y cortar en el punt0
#de frecuencia 

bb_min=np.where(psd_welch_ha>psd_welch_ha[bb_max[0][0]])
bw_min=f_welch_ha[bb_min[0][0]]


plt.figure(3)
plt.plot(f_welch_ha,psd_welch_ha,label="hamming")
plt.axvline(x=bw_max,color='r')
plt.axvline(x=bw_min,color="r")
