import numpy as np
from scipy import signal as sig

import matplotlib.pyplot as plt
   
import scipy.io as sio
from scipy.io.wavfile import write
import sounddevice as sd



fs_ecg = 1000 # Hz


mat_struct = sio.loadmat('./ECG_TP4.mat')

ecg_one_lead = mat_struct['ecg_lead']
N = len(ecg_one_lead)

ecg_sucio=ecg_one_lead[670000:700000,0].reshape(-1)

ecg_limpio= np.load('ecg_sin_ruido.npy')

promedios=20
zero_padding=2
nperseg=ecg_sucio.shape[0]//promedios


f_welch_ha , psd_welch_sucio = sig.welch(x=ecg_sucio, fs=fs_ecg ,window="hamming",nperseg = nperseg, nfft=zero_padding*nperseg)

f_welch_ha , psd_welch_limpio= sig.welch(x=ecg_limpio, fs=fs_ecg ,window="hamming",nperseg = nperseg, nfft=zero_padding*nperseg)


plt.figure(2)

plt.plot(f_welch_ha,10*np.log10(psd_welch_sucio))

plt.plot(f_welch_ha,10*np.log10(psd_welch_limpio))
plt.xlim(0,50)