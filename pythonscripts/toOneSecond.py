import os, wave, pyaudio
import numpy as np
from scipy.fftpack import fft, ifft
from os import listdir
from os.path import isfile, join
from numpy import NaN, Inf, arange, isscalar, asarray, array

#mypath = '/home/sense/Documents/testfolder'
#mypath = '/Users/Capodit3/Google Drive/splitAudiofiles'
#mypathS = '/Users/Capodit3/Google Drive/splitAudiofiles/splitted'

mypath  = '/Volumes/LstarR HDD/Redencio2013-2014/noise_5min'
mypathS = '/Volumes/LstarR HDD/Redencio2013-2014/noise_10sec'

mypath = '/Users/agentleman/Documents/Sensedata/data/conan'
mypathS = '/Users/agentleman/Documents/Sensedata/data/conan2'

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

def splitAudio(x, fram, rate, f, d):
	#range and rate of  the soundwave
	rangeS = fram/rate
	rateS = 0
	print 'rangeS: ', rangeS
	#print 'Timeframe in sec', ';frequence', ';sum', ';max', ';min', ';mean', ';median', ';frequency'

        
	for i in range(rangeS):
		FORMAT = pyaudio.paInt16
		CHANNELS = 1
		RATE = rate # 16000
		print 'rateS', rateS, 'rate', rateS + rate
		WAVE_OUTPUT_FILENAME = d + '/' + str(i) + '_'+f
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setnframes(fram)
		wf.setsampwidth(samp)
		#wf.setframerate((rate))
		wf.setframerate((rate))
		#wf.writeframes(x[rateS:rateS + rate])
		wf.writeframes(x[rateS:rateS + rate * 20])
		rateS = rateS + rate * 10
		#wf.writeframes(x[rateS:rateS + rate * 10])
		wf.close()


'''
    0:16000+16000*20
    
    '''



for f in onlyfiles:
	print mypath+'/'+f
	try:
		if not '.DS_Store' in f:
			print 'hi1'
			x = wave.open(mypath+'/'+f, "rb")
			print x
			#Extract Raw Audio from Wav File
			chan = x.getnchannels()
			#print 'number of channels ', chan
			#Returns number of audio channels (1 for mono, 2 for stereo).


			samp = x.getsampwidth()
			#print 'samplewidth ', samp
			#Returns sample width in bytes.

			rate = x.getframerate()
			#print 'frame rate ', rate
			#Returns sampling frequency.

			fram = x.getnframes()
			#print 'number of frames ', fram
			#Returns number of audio frames.
			x = x.readframes(fram)
			x = np.fromstring(x, 'Int16')
			print x, fram, rate, f, mypath
			splitAudio(x, fram, rate*2, f, mypathS)
			x.close()
	except:
		print '' #"Oops!"

