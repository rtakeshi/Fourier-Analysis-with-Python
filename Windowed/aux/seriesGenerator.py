
##Generate Temporal Series in the current directory

import numpy as np
import random
import pandas as pd
N = 2048
def sinA(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(0, 2*np.pi, N);

	for i in range(N):
		if(i >= N/2):
			f[i] = np.sin(2*np.pi*t[i])
		else:
			f[i] = np.sin(10*np.pi*t[i])

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('sinA.csv', sep=',', encoding='utf-8', index=False, header = False)

def sinB(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(0, 2*np.pi, N);

	for i in range(N):
		if(i <= N/2):
			f[i] = np.sin(2*np.pi*t[i])
		else:
			f[i] = np.sin(10*np.pi*t[i])

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('sinB.csv', sep=',', encoding='utf-8', index=False, header = False)



def gaussianChirp(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(-3, 3, N);
	f = np.exp(-((2*np.pi)-(0+1j)*(6*np.pi))*t**2)

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('gauChirp.csv', sep=',', encoding='utf-8', index=False, header = False)


def linearChirp(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(0, 10, N);
	f = np.exp((0+1j)*(1/4)*t**2)

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('linearChirp.csv', sep=',', encoding='utf-8', index=False, header = False)


def quadraticChirp(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(-4, 4, N);
	f = np.exp((0+1j)*(1/4)*t**3)

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('quadChirp.csv', sep=',', encoding='utf-8', index=False, header = False)


def hiperbolicChirp(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(0, 10, N);
	f = np.cos((6*np.pi)/(2.3-t))

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('hiperChirp.csv', sep=',', encoding='utf-8', index=False, header = False)

def whiteNoise(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(1, N, N);
	mean = 0
	std = 1 
	num_samples = 1024
	f = np.random.normal(mean, std, size=num_samples)

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('whiteNoise.csv', sep=',', encoding='utf-8', index=False, header = False)


def pulse(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(1, N, N);

	i = 0
	for k in range(N):
		if (k == int(N/2)):
			f[i] = 1
		else:
			f[i] = 0
		i += 1


	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('pulse.csv', sep=',', encoding='utf-8', index=False, header = False)


def mensalSerie(N):
	t = np.zeros(N)
	f = np.zeros(N)
	dataToFile = pd.DataFrame()
	t = np.linspace(1, 50, N);
	tData = t/12
	i = 0
	for x in tData:
		if (t[i]>=20 and t[i]<=30):
			f1 = 10
			f2 = 5
		else:
			f1 = 10
			f2 = 3
		f[i] = np.cos(2*np.pi/f1*t[i]) + np.cos(2*np.pi/f2*t[i]) + random.uniform(0, 10)*0.01
		i+=1

	dataToFile['t'] = t
	dataToFile['f'] = f


	dataToFile.to_csv('mensalSerie.csv', sep=',', encoding='utf-8', index=False, header = False)







sinA(N)
sinB(N)
'''
pulse(N)

gaussianChirp(N)
linearChirp(N)
quadraticChirp(N)
hiperbolicChirp(N)
whiteNoise(N)
mensalSerie(N)
'''