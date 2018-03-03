#exec(open("janelada.py").read(),globals())

###CHECAR A INTEGRAÇÃO SFW###

import numpy as np
import scipy as sp
import time
import matplotlib.pyplot as plot
import pandas as pd
import windowsFourier as winFourier
import generateLatex as lt
import random

ltx = open("figs.txt", 'w')

dataList = []
dataList.append("sinA.csv")
dataList.append("sinB.csv")
dataList.append("gauChirp.csv")
dataList.append("linearChirp.csv")
dataList.append("quadChirp.csv")
dataList.append("hiperChirp.csv")
dataList.append("mensalSerie.csv")
dataList.append("whiteNoise.csv")
dataList.append("jao.csv")
dataList.append("sunspot.csv")
dataList.append("nino3.csv")



eqList = []

eqList.append("eqpapoulis.png")
eqList.append("eqtukey.png")
eqList.append("eqtukey.png")
eqList.append("eqtukey.png")
eqList.append("eqbartllet.png")
eqList.append("eqboxcar.png")
eqList.append("eqhamming.png")
eqList.append("eqhanning.png")


sectionList = []
sectionList.append("Dois Senos com Localização Temporal Diferenciada  A")
sectionList.append("Dois Senos com Localização Temporal Diferenciada  B")
sectionList.append("Chirp Gaussiano")
sectionList.append("Chirp Linear")
sectionList.append("Chirp Quadratico")
sectionList.append("Chirp Hiperbolico")
sectionList.append("Série Mensal")
sectionList.append("Ruído Branco")
sectionList.append("NINO3 Temperatura da Superfície do Mar")
sectionList.append("Wolf\'s Numero de Manchas Solares")
sectionList.append("Oscilações Árticas")


sectionIndex = 0



windowSizes = []

windowSizes.append(16)
windowSizes.append(64)
windowSizes.append(128)


fNumber = 1

latexString = ""

for data in dataList:
	latexString += lt.includeSection(sectionList[sectionIndex])
	print(data)
	for size in windowSizes:
		
		dataFile = pd.read_csv('data/'+data, names = ['t', 'f'], sep=',')
		spectogramPower = pd.DataFrame()
		spectogramPhase = pd.DataFrame()

		#t = np.linspace(0, 2*np.pi, N);

		t = dataFile['t']
		f = dataFile['f'].apply(lambda x: np.complex(x))
		N = f.size
		Nwin = size  #Define Window Length(Non-zero value)
		

		###########################################################################################

		Nwin *= 2
		#print("1 - Papoulis\n2 - Tukey\n3 - Barllet\n4 - Box Car\n5 - Hamming\n6 - Hanning")
		#choice = int(input("Chose window for Analysing the Signal: "))
		wName = ""
		eqIndex = 0
		for choice in range(1, 9):
			
			if(choice == 1):
				if(size != 16):
					pass
				else:
					window, twindow = winFourier.papoulisWindow(Nwin)
					wName = "PapoulisWindow"
					wNameP = "Papoulis Window "
			elif(choice == 2):
				if(size != 16):
					pass
				else:
					beta = 0
					window, twindow = winFourier.tukeyWindow(Nwin, beta)
					wName = "TukeyWindow(beta" + str(beta).replace('.', '') + ")" 
					wNameP = "Tukey Window (beta " + str(beta) + ") " 
			elif(choice == 3):
				if(size != 16):
					pass
				else:
					beta = 0.15
					window, twindow = winFourier.tukeyWindow(Nwin, beta)
					wName = "TukeyWindow(beta" + str(beta).replace('.', '') + ")" 
					wNameP = "Tukey Window (beta " + str(beta) + ") " 
			elif(choice == 4):
				if(size != 16):
					pass
				else:
					beta = 0.3
					window, twindow = winFourier.tukeyWindow(Nwin, beta)
					wName = "TukeyWindow(beta"+ str(beta).replace('.', '') + ")" 
					wNameP = "Tukey Window (beta " + str(beta) + ") " 
			elif(choice == 5):
				if(size != 16):
					pass
				else:
					window, twindow = winFourier.bartlletWindow(Nwin)
					wName = "BartlletWindow"
					wNameP = "Bartllet Window "
			elif(choice == 6):
				window, twindow = winFourier.boxCarWindow(Nwin)
				wName = "BoxCarWindow"
				wNameP = "Box Car Window "
			elif(choice == 7):
				if(size != 16):
					pass
				else:
					window, twindow = winFourier.hammingWindow(Nwin)
					wName = "HammingWindow"
					wNameP = "Hamming Window "
			elif(choice == 8):
				window, twindow = winFourier.hanningWindow(Nwin)
				wName = "HanningWindow"
				wNameP = "Hanning Window "

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


				fw = f*windowSlide

				fwhat = np.fft.fft(fw)
				fwhatshift = np.fft.fftshift(fwhat/N)
				energy = (abs(fwhatshift)**2); 
				columName = "t"+str(i)


				spectogramPower[columName] = energy




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

			plot.ylim(-1.5, 1.5)
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

			if(wFFTfreq.size != wEnergy.size):
				eqIndex += 1
				plot.close()
				pass
			else:
				###Plot###
				ax4 = fig.add_axes([0.92, 0.75, 0.075, 0.2])
				ax4.plot(wFFTfreq, wEnergy, 'k-', linewidth=1.5)
				ax4.set_title("ĝ", fontsize=16)
				ax4.tick_params(axis='both', labelsize=16)
				plot.xlim(-1.5, 1.5)


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
				#ax5.plot(sfw, freq, 'k--')
				ax5.plot(energy, freq,'-', color=[0.7, 0.7, 0.7],
				        linewidth=1.)
				#legend = ax5.legend(("FT"), fontsize="small")
				#legend.get_frame().set_facecolor('none')
				#legend.get_frame().set_edgecolor('w')
				ax5.set_title('Spectrum', fontsize=16)
				plot.ylim(-0.7, 0.7)
				ax5.tick_params(axis='both', labelsize=16)


				ax5.invert_yaxis()


				################################################################
				fname = str(fNumber)+data[0:-4]+wName+str(int(Nwin/2))+'.pdf'
				plot.savefig('figs/'+fname, bbox_inches='tight')
				plot.close()

				latexString += lt.includeFig('figs/'+fname, sectionList[sectionIndex])
				latexString += lt.includeEq(choice, wNameP+str(int(Nwin/2))+" points")
				eqIndex += 1

	fNumber += 1
	sectionIndex += 1

ltx.write(latexString)
ltx.close()

