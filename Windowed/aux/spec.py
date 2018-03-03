import matplotlib.pyplot as plt
import numpy as np

N = 1024
Nwin = N/4  #Define Window Length(Non-zero value)
t = np.zeros(N)
f = np.zeros(N)


t = np.linspace(0, 2*np.pi, N);


for i in range(N):
	if(i >= N/2):
		f[i] = np.sin(2*np.pi*t[i])
	else:
		f[i] = np.sin(10*np.pi*t[i])

k = np.linspace(-(N/2), N/2-1, N);
freq = (k*2*np.pi)/N;

fhat = np.fft.fft(f)
fhatshift = np.fft.fftshift(fhat/N)
energy = (abs(fhatshift)**2); 



fig, (ax1, ax2)= plt.subplots(2)

ax1.plot(t, f, color='black')
ax1.set_xlabel('T')
ax1.set_ylabel('F')

ax2.plot(freq, energy, color='black')
ax2.set_xlabel('freq')
ax2.set_ylabel('energy')
plt.xlim(0, 3)


plt.show()