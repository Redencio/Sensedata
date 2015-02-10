from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

import os
from os import listdir
from os.path import isfile, join

'''mypath_noise  = '/Volumes/LstarR HDD/Redencio2013-2014/geluidsbestanden/noise1'
mypath_speech  = '/Volumes/LstarR HDD/Redencio2013-2014/geluidsbestanden/stem2'
'''

mypath_noise  =  "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundNoise/"
mypath_speech  = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundSpeech/"

#mypath_noise = '/Volumes/LstarR HDD/Redencio2013-2014/noise_10sec'
#mypath_speech = '/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs'

onlyfiles = [ f for f in listdir(mypath_noise) if isfile(join(mypath_noise,f)) ]
mypath_speech = [ f for f in listdir(mypath_speech) if isfile(join(mypath_speech,f)) ]
csv = open("melfeatures_PlusFilename_no2Jos_new.csv", "w")
header = 'speech, Avgf0, Avgf1, Avgf2, Avgf3, Avgf4, Avgf5, Avgf6, Avgf7, Avgf8, Avgf9, Avgf10, Avgf11, Avgf12, filename'
csv.write(header)
csv.write('\n')

def writeMelToCSV(logMelFeats):
    csv.write('no')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))

def writeMelToCSVspeech(logMelFeats):
    csv.write('yes')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))



for file in onlyfiles:
    if not file == '.DS_Store':
        #(rate,sig) = wav.read("/Users/Capodit3/Documents/Sensedata/sense-os project2/noise/"+file)
        (rate,sig) = wav.read("/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundNoise/"+file)
        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)
        sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)
        sum_feat = sum_feat[0:13]
        writeMelToCSV(sum_feat)
        print 'Non: ', sum_feat[0:13]
        csv.write(','+file+'\n')

'''
for file in mypath_speech:
    if not file == '.DS_Store':
        #(rate,sig) = wav.read("/Users/Capodit3/Documents/Sensedata/sense-os project2/speech/"+file)
        (rate,sig) = wav.read("/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundSpeech/"+file)
        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)
        sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)
        sum_feat = sum_feat[0:13]
        writeMelToCSVspeech(sum_feat)
        print 'Adje: ', sum_feat[0:13]
        csv.write(','+file+'\n')
'''
#writeMelToCSV(sum_feat)
csv.close()

'''
    print rate, len(sig)
    mfcc_feat = mfcc(sig,rate)
    fbank_feat = logfbank(sig,rate)
    
    print len(fbank_feat), len(mfcc_feat)
    
    sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)#, fbank_feat[1:13,:]
    
    sum_feat = sum_feat[0:13]
    '''