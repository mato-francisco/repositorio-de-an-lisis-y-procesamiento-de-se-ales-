import numpy as np
from scipy import signal
from scipy.fft import fft, fftshift
import matplotlib.pyplot as plt


hamming = signal.windows.hamming(51)
blackmanharris = signal.windows.blackmanharris(51)
flattop = signal.windows.flattop(51)
# plt.figure(1)
# plt.plot(hamming)
# plt.plot(blackmanharris)
# plt.plot(flattop)
# plt.ylabel("Amplitude")
# plt.xlabel("Sample")



plt.figure(2)
#hamming------------------
fft_hamming = fft(hamming, 2048) / (len(hamming)/2.0)
freq = np.linspace(-0.5, 0.5, len(fft_hamming))
response_hamming = 20 * np.log10(np.abs(fftshift(fft_hamming / abs(fft_hamming).max())))


#blackmanharris----------------
fft_blackmanharris = fft(blackmanharris, 2048) / (len(blackmanharris)/2.0)
freq = np.linspace(-0.5, 0.5, len(fft_blackmanharris))
response_blackmanharris = 20 * np.log10(np.abs(fftshift(fft_blackmanharris / abs(fft_blackmanharris).max())))

#flattop----------------------------------

fft_flattop= fft(flattop, 2048) / (len(flattop)/2.0)
freq = np.linspace(-0.5, 0.5, len(fft_flattop))
response_flattop = 20 * np.log10(np.abs(fftshift(fft_flattop / abs(fft_flattop).max())))





plt.plot(freq, response_hamming, label="hamming",linestyle='-',marker='' ,color='b')
plt.plot(freq, response_blackmanharris, label="blackmanharris",linestyle='-',marker='' ,color='r')
plt.plot(freq, response_flattop, label="blackmanharris",linestyle='-',marker='' ,color='g')
plt.legend()
plt.axis([-0.5, 0.5, -120, 0])
plt.ylabel("db normalizada")
plt.xlabel("frecuencia normalizada")