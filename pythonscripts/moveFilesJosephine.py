import csv
from pydub import AudioSegment
import os, shutil
from os import listdir
from os.path import isfile, join

#path = "/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/audiofiles/splitted/"
path = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesound/"
#pathN = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesoundNoise/"


#path = "/Volumes/LstarR HDD/Redencio2013-2014/josephinesound/"
pathS = "/Volumes/LstarR HDD/Redencio2013-2014/josSpeech/"
pathN = "/Volumes/LstarR HDD/Redencio2013-2014/josNoise/"

#csv = open('tekstJosephine.csv', 'rb')
with open('afgeluisterde bestandenJosje.csv', 'rU') as csvfile:

	file = csv.reader(csvfile, delimiter=';')
	count = 0
	for line in file:
		columns = line
		filename = columns[3]
		speech = columns[5]
		
		if speech == '':	
			break;

		if not speech == 'gesprek':
			speech = int(columns[5])


		if speech == 0 and not filename == 'opnamenaam':
			shutil.move(path+filename, pathN+filename)
			print speech, filename
			
		if speech == 1 and not filename == 'opnamenaam':
			shutil.move(path+filename, pathS+filename)
			print speech, filename

		#if speech == 0 and not filename == 'opnamenaam':
			#shutil.move(path+filename, pathN+filename)
			#print speech, filename
			
		count += 1