# aaja ko kakshha ma hami package installation ko bare ma sikxaum
#  jun bata signal processing jasta kaam haru garna sakxaum

import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

fs, A, f = 500, 1, 20
t = np.arange(0,5,1/fs)

#  signal generation
sig = A*np.sin(2*np.pi*2*t)
noise = 2*np.sin(2*np.pi*30*t)+1.5*np.sin(2*np.pi*40*t)
noisySig = sig + noise

# fft analysis
fft_sig = np.abs(np.fft.fft(noisySig))
fft_sig = fft_sig[1:251]

# signal filtration
order, cutoff = 40, 15
filterLP = signal.butter(order, cutoff, 'lp', fs=fs, output='sos')
filteredSignal = signal.sosfilt(filterLP, noisySig)

plt.figure()
plt.subplot(411)
plt.plot(t,sig)
plt.subplot(412)
plt.plot(t,noisySig)
plt.subplot(413)
plt.plot(fft_sig)
plt.subplot(414)
plt.plot(t,filteredSignal)
plt.show()




