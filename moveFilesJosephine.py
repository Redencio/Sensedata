import csv
from pydub import AudioSegment
import os, shutil
from os import listdir
from os.path import isfile, join

path = "/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/audiofiles/splitted/"
#pathS = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundSpeech/"
#pathN = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundNoise/"


#path = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesound/"
pathS = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundSpeech/"
pathN = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundNoise/"

#csv = open('tekstJosephine.csv', 'rb')
csv = open('audio2Handmatig.csv', 'rb')

for line in csv.readlines():
    columns = line.split(';')
    filename = columns[0]
    speech = columns[1]
    print speech
    if not speech == 'answer':
        speech = int(columns[1])
    
    if speech == 1 and not filename == 'audio':
        shutil.move(path+filename, pathS+filename)


    if speech == 0 and not filename == 'audio':
        shutil.move(path+filename, pathN+filename)
