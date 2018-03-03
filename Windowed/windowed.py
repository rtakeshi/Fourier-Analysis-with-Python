#exec(open("janelada.py").read(),globals())

import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plot
import pandas as pd
import windowsFourier as winFourier
import random


fname = "sinA" #File Name
dataFile = pd.read_csv('data/'+fname+".csv", names = ['t', 'f'], sep=',') #Pandas DataFrame For CSV Files (time, data)
spectogramPower = pd.DataFrame()

t = dataFile['t']
f = dataFile['f'].apply(lambda x: np.complex(x))
N = f.size
Nwin = 32 #Window Size


###########################################################################################

print("1 - Papoulis\n2 - Tukey\n3 - Barllet\n4 - Box Car\n5 - Hamming\n6 - Hanning")
choice = int(input("Chose window for Analysing the Signal: "))
wName = ""
Nwin = 2*Nwin
if(choice == 1):
	window, twindow = winFourier.papoulisWindow(Nwin)
	wName = "Papoulis Window"
elif(choice == 2):
	beta = int(input("Chose beta (0, 0.15, 0.3): "))
	window, twindow = winFourier.tukeyWindow(Nwin, beta)
	wName = "Tukey Window (beta: " + str(beta) + ")" 
elif(choice == 3):
	window, twindow = winFourier.barlletWindow(Nwin)
	wName = "Barllet Window"
elif(choice == 4):
	window, twindow = winFourier.boxCarWindow(Nwin)
	wName = "Box Car Window"
elif(choice == 5):
	window, twindow = winFourier.hammingWindow(Nwin)
	wName = "Hamming Window"
elif(choice == 6):
	window, twindow = winFourier.hanningWindow(Nwin)
	wName = "Hanning Window"

wFunction = np.zeros(int(Nwin/2))



i = 0
for x in window:
	if (x!=0):
		wFunction[i] = x
		i+=1

i = 0
k = 0
j = 0
zeroFilling = 0 
wFunctionIndex = 0

windowSlide = window


#Sliding Window through time
for i in range(N):
	windowSlide = np.zeros(N)
	
	if (i-len(wFunction)-1 < 0):
		endIndex = 0
	else:
		endIndex = i-len(wFunction)


	wFunctionIndex = len(wFunction)-1
	endWindow = 0

	for endWindow in range(i, endIndex-1, -1):
		windowSlide[endWindow] = wFunction[wFunctionIndex]
		wFunctionIndex -= 1

	for k in range(endWindow, 0, -1):
		windowSlide[k] = 0
		
	for j in range(i, N-1):
		windowSlide[j] = 0

	#Something like Convolution
	fw = f*windowSlide

	##FFT To spectogram column
	fwhat = np.fft.fft(fw)
	fwhatshift = np.fft.fftshift(fwhat/N)
	energy = (abs(fwhatshift)**2); 
	columName = "t"+str(i)


	spectogramPower[columName] = energy



###Figure Generator

fig = plot.figure(figsize=(21, 14))
#plot.suptitle(wName+' with '+str(int(Nwin/2))+' points ', fontsize=16)

#####################Function###############
ax1 = fig.add_axes([0.1, 0.75, 0.65, 0.2])
ax1.plot(t, f, 'k', linewidth=1.5)
ax1.set_xlabel('Time', fontsize=16)
ax1.tick_params(axis='both', labelsize=16)
plot.xlim(min(t), max(t))



####################SPECTOGRAM################
###'frequency calc'
k = np.linspace(-(N/2), N/2-1, N);
freq = (k*2*np.pi)/N;
#period = 1/freq
#print(freq)

ax2 = fig.add_axes([0.1, 0.40, 0.65, 0.2])
imgax2= ax2.contourf(t, freq, spectogramPower)
ax2.set_xlabel('')
ax2.set_ylabel('Freq')
ax2.tick_params(axis='both', labelsize=16)

plot.ylim(-1, 1)
cbar = plot.colorbar(imgax2, orientation='horizontal', fraction=0.1, pad=0.1)
cbar.ax.tick_params(labelsize=14) 
ax2.invert_yaxis()



####################Window Function################


ax3 = fig.add_axes([0.80, 0.75, 0.075, 0.2])
ax3.plot(twindow, window, 'k-', linewidth=1.5)
ax3.set_title("g", fontsize=16)
ax3.tick_params(axis='both', labelsize=16)


####################Window Function FFT################
###Calc###
wFFTk = np.linspace(-(Nwin/2), Nwin/2-1, Nwin);
wFFTfreq = (wFFTk*2*np.pi)/Nwin;
#wFFTperiod = 1/wFFTfreq

windowHat = np.fft.fft(window)
windowHatShift = np.fft.fftshift(windowHat/Nwin)
wEnergy = (abs(windowHatShift)**2); 

###Plot###
ax4 = fig.add_axes([0.92, 0.75, 0.075, 0.2])
ax4.plot(wFFTfreq, wEnergy, 'k-', linewidth=1.5)
ax4.set_title("ĝ", fontsize=16)
ax4.tick_params(axis='both', labelsize=16)
plot.xlim(-1, 1)


####################FFT SFW################
###CALC
specMatrix = spectogramPower.as_matrix()
sfw = np.zeros(N)

for i in range(N):
	sfw[i] = np.trapz(specMatrix[i], t)

fhat = np.fft.fft(f)
fhatshift = np.fft.fftshift(fhat/N)
energy = np.abs(fhatshift)**2



###PLOT

ax5 = fig.add_axes([0.80, 0.43, 0.18, 0.17])
ax5.plot(sfw, freq, 'k--')
ax5.plot(energy, freq,'-', color=[0.7, 0.7, 0.7],
        linewidth=1.)
legend = ax5.legend(("SFW", "FT"), fontsize="small")
legend.get_frame().set_facecolor('none')
legend.get_frame().set_edgecolor('w')
ax5.set_title('Spectrum', fontsize=16)
plot.ylim(-1, 1)
ax5.tick_params(axis='both', labelsize=16)


ax5.invert_yaxis()


################################################################
plot.show()
plot.savefig("figs/"+fname+wName+str(int(Nwin/2))+'.pdf', bbox_inches='tight')









'''
	#SPECTOGRAM PHASE

	#theta = arctan(b/a) {-pi/2, pi/2}

	#np.arctan; (parte imag/real)
	#Ajuste do quadrante:
	# Se a > 0 = arctan(b/a)
	# Se a<0, b>=0 = arctan(b/a) + pi
	# Se a <0, b< 0 = arctan(b/a) - pi
	# Se a = 0, b >= 0 = pi/2
	# Se a = 0, b<0 = -pi/2
	phase = np.zeros(N)
	indexPhase = 0
	for ip in fwhatshift:
		b = ip.imag
		a = ip.real
		if (a > 0):
			phase[indexPhase] = np.arctan(b/a)
		elif (a<0 and b>=0):
			phase[indexPhase] = np.arctan(b/a)+np.pi
		elif (a<0 and b<0):
			phase[indexPhase] = np.arctan(b/a)-np.pi
		elif (a == 0 and b >= 0):
			phase[indexPhase] = np.pi/2
		elif (a == 0 and b < 0):
			phase[indexPhase] = np.pi/2*(-1)

	phaseColumn = 'p'+str(i)
	spectogramPhase[phaseColumn] = phase
'''
