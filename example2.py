from features import mfcc
from features import logfbank
import scipy.io.wavfile as wav

import os
from os import listdir
from os.path import isfile, join

'''mypath_noise  = '/Volumes/LstarR HDD/Redencio2013-2014/geluidsbestanden/noise1'
mypath_speech  = '/Volumes/LstarR HDD/Redencio2013-2014/geluidsbestanden/stem2'
'''

mypath_noise  =  "/Volumes/LstarR HDD/Redencio2013-2014/noise_sec2/"
mypath_speech  = "/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs4_5_sec2/"

#mypath_noise = '/Volumes/LstarR HDD/Redencio2013-2014/noise_10sec'
#mypath_speech = '/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs'

onlyfiles = [ f for f in listdir(mypath_noise) if isfile(join(mypath_noise,f)) ]
mypath_speech = [ f for f in listdir(mypath_speech) if isfile(join(mypath_speech,f)) ]
csv = open("mel1stdv.csv", "w")
header = 'speech,Avgf0,stdv0,Avgf1,stdv1,Avgf2,stdv2,Avgf3,stdv3,Avgf4,stdv4,Avgf5,stdv5,Avgf6,stdv6,Avgf7,stdv7,Avgf8,stdv8,Avgf9,stdv9,Avgf10,stdv10,Avgf11,stdv11,Avgf12,stdv12,filename'
csv.write(header)
csv.write('\n')

#stdev()

def writeMelToCSV(logMelFeats, stdv):
    csv.write('0')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))
        csv.write(',')
        csv.write(str(stdv))

def writeMelToCSVspeech(logMelFeats):
    csv.write('1')
    for feat in logMelFeats:
        csv.write(',')
        csv.write(str(feat))



for file in onlyfiles:
    if not file == '.DS_Store':
        #(rate,sig) = wav.read("/Users/Capodit3/Documents/Sensedata/sense-os project2/noise/"+file)
        (rate,sig) = wav.read("/Volumes/LstarR HDD/Redencio2013-2014/noise_sec2/"+file)
        mfcc_feat = mfcc(sig,rate)
        fbank_feat = logfbank(sig,rate)
        stdv = stdev()
        sum_feat = sum(fbank_feat[:,:])/len(fbank_feat)
        sum_feat = sum_feat[0:13]
        writeMelToCSV(sum_feat, stdv)
        print 'Non: ', sum_feat[0:13]
        csv.write(','+file+'\n')

'''
for file in mypath_speech:
    if not file == '.DS_Store':
        #(rate,sig) = wav.read("/Users/Capodit3/Documents/Sensedata/sense-os project2/speech/"+file)
        (rate,sig) = wav.read("/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs4_5_sec2/"+file)
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