from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

import os
from os import listdir
from os.path import isfile, join

#mypath_noise  = '/Users/Capodit3/Documents/Sensedata/sense-os project2/noise'
#mypath_speech  = '/Users/Capodit3/Documents/Sensedata/sense-os project2/speech'

mypath_noise = "/Users/agentleman/Documents/Sensedata/data/youtube_noise"
#mypath_speech = '/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs'
mypath_speech = "/Users/agentleman/Documents/Sensedata/data/youtube_speech"
mypath_speech2 = "/Users/agentleman/Documents/Sensedata/data/youtube_speech"

onlyfiles = [ f for f in listdir(mypath_noise) if isfile(join(mypath_noise,f)) ]
mypath_speech = [ f for f in listdir(mypath_speech) if isfile(join(mypath_speech,f)) ]
csv = open("mfcc-youtube.csv", "w")
header = 'speech, Avgf0, Avgf1, Avgf2, Avgf3, Avgf4, Avgf5, Avgf6, Avgf7, Avgf8, Avgf9, Avgf10, Avgf11, Avgf12, filename'
csv.write(header)
csv.write('\n')

def writeMelToCSV(logMelFeats):
    csv.write('0')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))

def writeMelToCSVspeech(logMelFeats):
    csv.write('1')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))



for file in onlyfiles:
    if not file == '.DS_Store':
        #(rate,sig) = wav.read("/Users/Capodit3/Documents/Sensedata/sense-os project2/noise/"+file)
        (rate,sig) = wav.read(mypath_noise+"/"+file)
        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)
        sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)
        sum_feat = sum_feat[0:13]
        writeMelToCSV(sum_feat)
        print 'Non: ', sum_feat[0:13]
        csv.write(','+file+'\n')

count = 0

for file in mypath_speech:
    if not file == '.DS_Store':
        (rate,sig) = wav.read(mypath_speech2+"/"+file)
        #(rate,sig) = wav.read("/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs/"+file)
        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)
        sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)
        sum_feat = sum_feat[0:13]
        writeMelToCSVspeech(sum_feat)
        print 'Adje: ', sum_feat[0:13]
        #if count >= 705:
        #	break;
        #count += 1
        csv.write(','+file+'\n')

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