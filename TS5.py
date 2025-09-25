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

plt.figure()
plt.plot(wav_data)

promedios=100
zero_padding=1
nperseg=wav_data.shape[0]//promedios

f_welch , psd_welch=sig.welch(x=wav_data, fs=fs_audio ,window="hamming",nperseg = nperseg,nfft=zero_padding*nperseg)

plt.figure(2)

plt.plot(f_welch,psd_welch)


sd.play(wav_data, fs_audio)

