import numpy as np


def papoulisWindow(N):
	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i])<=(0.5)):
			window[i] = (1/np.pi)*np.abs(np.sin(2*np.pi*twindow[i]))+(1-2*np.abs(twindow[i]))*np.cos(2*np.pi*twindow[i])
		else:
			window[i] = 0
		i+=1
	return window, twindow

def tukeyWindow(N, beta):
	'''
	beta values = 0.3, 0.15, 0
	'''

	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i])<=beta):
			window[i] = 1
		elif (beta <= np.abs(twindow[i]) and np.abs(twindow[i]) <= 1/2):
			window[i] = 1/2 + 1/2*np.cos((2*np.pi*np.abs(twindow[i])-beta)/1-2*beta)
		else:
			window[i] = 0
		i+=1
	return window, twindow

def bartlletWindow(N):
	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i]) <= 0.5):
			window[i] = (1-2*np.abs(twindow[i]))
		else:
			window[i] = 0
		i+=1
	return window, twindow

def boxCarWindow(N):
	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i]) <= 0.5):
			window[i] = 1
		else:
			window[i] = 0
		i+=1
	return window, twindow

def hammingWindow(N):
	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i]) <= 0.5):
			window[i] = 0.54+0.46*np.cos(2*np.pi*twindow[i])
		else:
			window[i] = 0
		i+=1
	return window, twindow

def hanningWindow(N):
	twindow = np.linspace(-1, 1, N)
	i = 0
	window = np.zeros(int(N))
	##Window Function
	for x in twindow:
		if (np.abs(twindow[i]) <= 0.5):
			window[i] = 0.5+0.5*np.cos(2*np.pi*twindow[i])
		else:
			window[i] = 0
		i+=1
	return window, twindow