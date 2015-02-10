from pydub import AudioSegment
import os, shutil
from os import listdir
from os.path import isfile, join

path = "/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs"
path2 = "/Volumes/LstarR HDD/Redencio2013-2014/speech corpus48_wavs5_6/"

speech_file = [ f for f in listdir(path) if isfile(join(path,f)) ]

for file in speech_file:
	
	if not file == '.DS_Store':
		sound = AudioSegment.from_wav(path+'/'+file)

		#print 'Hi', sound.duration_seconds

		if sound.duration_seconds > 5 and sound.duration_seconds <=6 :
			shutil.move(path+'/'+file, path2+file)