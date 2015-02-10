import os
from os import listdir
from os.path import isfile, join

mypath  = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/audiofiles/splitted' 

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
toFile = "audio.csv"
csv = open(toFile, "w")

header = 'audio_url,answer'
url = 'http://audiofiles.dev.sense-os.nl/'

count = 0
n = 1

csv.write(header)

for file in onlyfiles:
	if count == 1000:
		csv.close()
		csv = open(str(n)+'_'+toFile, "wb")
		csv.write(header)

	audio = url + file+','
	csv.write("\n")
	if len(file) > 9:
		csv.write(audio)

	count = count + 1

csv.close()
