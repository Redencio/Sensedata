from pydub import AudioSegment
import os, shutil
from os import listdir
from os.path import isfile, join

path = "/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise"
path2 = os.getcwd()

print path2


speech_file = [ f for f in listdir(path) if isfile(join(path,f)) ]



def move(directory, files):
	#files = [ f for f in listdir(speech_file) if isfile(join(speech_file,f)) ]

	for file in files:
	
		if not file == '.DS_Store':
			sound = AudioSegment.from_wav(path+'/'+directory+'/'+file)

			#if sound.duration_seconds > 5 and sound.duration_seconds <=6 :
			shutil.move(path+'/'+directory+'/'+file, path2+file)


for file in speech_file:
	subfile = [ f for f in listdir(path) ]


for sub in subfile:
    if not sub == '.DS_Store':
        files = [ f for f in listdir(path+'/'+sub) if isfile(join(path+'/'+sub,f)) ]
        move(sub, files)