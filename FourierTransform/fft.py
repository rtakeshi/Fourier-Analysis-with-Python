#exec(open("janelada.py").read(),globals())

###CHECAR A INTEGRAÇÃO SFW###

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import pandas as pd

fName = "nino3"
dataFile = pd.read_csv('data/'+fName+".csv", names = ['t', 'f'], sep=',')
spectogramPower = pd.DataFrame()
spectogramPhase = pd.DataFrame()


t = dataFile['t']
f = dataFile['f'].apply(lambda x: np.complex(x))
N = f.size





###########################################################################################
k = np.linspace(-(N/2), N/2-1, N);
freq = (k*2*np.pi)/N;


fhat = np.fft.fft(f)
fhatshift = np.fft.fftshift(fhat/N)
energy = np.abs(fhatshift)**2



plt.figure(figsize=(6, 4))
ax1 = plt.subplot(2, 1, 1,)
ax1.plot(t, f, color='black')
ax1.set_xlabel("t")
ax1.set_ylabel("f(t)")

ax1.set_xlim(np.min(t), np.max(t))

ax2 = plt.subplot(2, 1, 2)
ax2.plot(freq, energy, color='black')
ax2.set_xlabel("freq")
ax2.set_ylabel("coeficientes de Fourier")

ax2.set_title('Spectrum')
ax2.set_xlim(0, 0.5)

plt.tight_layout()

#plt.show()

################################################################

plt.savefig(fName+"spectrum.eps")







