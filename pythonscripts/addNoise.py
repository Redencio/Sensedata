from pydub import AudioSegment
import os, shutil
from os import listdir
from os.path import isfile, join

#sound1 = AudioSegment.from_wav("/Users/Capodit3/Documents/Sensedata/sense-os project2/17_ch16.wav")
#sound2 = AudioSegment.from_wav("/Users/Capodit3/Documents/Sensedata/sense-os project2/a0374 10.wav")

#combined = sound1.overlay(sound2)

#combined.export("/Users/Capodit3/Documents/Sensedata/sense-os project2/combined.wav", format='wav')

# recorded voices
speechCorpus = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/speechCorpusMax9'

#recorded noise on different locations
#kitchen = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise/DKITCHEN2'
hallway = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise/OHALLWAY2'
office = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise/OOFFICE2'
park = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise/NPARK2'
#living = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/noise/DLIVING3'


speech = [ f for f in listdir(speechCorpus) if isfile(join(speechCorpus,f)) ]
#kitchen_onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
hallway_onlyfiles = [ f for f in listdir(hallway) if isfile(join(hallway,f)) ]
office_onlyfiles = [ f for f in listdir(office) if isfile(join(office,f)) ]
park_onlyfiles = [ f for f in listdir(park) if isfile(join(park,f)) ]
#living_onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]


counter = 0

## Overfitting by using the same noise
## Overfitting by using the same speech


'''
Add speech later in the recording of noise.
'''
def addNoiseLater(pathTosound1, pathTosound2, fileName, type):
	# count seconds of the speech data
	seconds = pathTosound2.duration_seconds * 1000
	
	first_seconds = pathTosound1[:seconds]
	last_seconds = pathTosound1[-seconds:]
	combined = last_seconds.overlay(pathTosound2)
	reunite = first_seconds.append(combined)
	writeOutfile(reunite, "addNoiseLater", fileName, type)


'''
Add speech first in the recording of noise.
'''
def addNoiseFirst(pathTosound1, pathTosound2, fileName, type):
	combined = pathTosound1.overlay(pathTosound2)
	writeOutfile(combined, "addNoiseFirst", fileName, type)

'''
Add speech in the middle of the recording of noise.
'''
def addNoiseBetween(pathTosound1, pathTosound2, fileName, type):
	# count seconds of the speech data
	seconds = pathTosound1.duration_seconds * 1000
	seconds2 = pathTosound2.duration_seconds * 1000
    
	#print seconds, seconds2
	clipseconds = seconds - (seconds2 + seconds2/2)
	ends = seconds - seconds2/2

	beginning = pathTosound1[: clipseconds]
	end = pathTosound1[-clipseconds:]
	middle = pathTosound1[clipseconds:ends]
	
	combined = middle.overlay(pathTosound2)
	print "pathTosound2", pathTosound2, fileName
	reunite = beginning.append(combined)
	reunite = reunite.append(end)
	writeOutfile(reunite, "addNoiseBetween", fileName, type)

'''
Add speech at the beginning and end of the recording of noise.
'''
def addNoiseWrap(pathTosound1, pathTosound2, fileName, type):
	seconds = pathTosound1.duration_seconds * 1000
	seconds2 = pathTosound2.duration_seconds * 1000
	#print seconds, seconds2
	clipseconds = seconds - (seconds2 + seconds2/2)
	split_seconds = seconds2/2
	ends = seconds - seconds2/2

	beginning = pathTosound1[:clipseconds]
	end = pathTosound1[-clipseconds:]
	middle = pathTosound1[clipseconds:ends]
	
	combined_beginning = beginning.overlay(pathTosound2[: clipseconds])
	combined_end = end.overlay(pathTosound2[-clipseconds:])

	
	reunite = combined_beginning.append(middle)
	reunite = reunite.append(combined_end)
	writeOutfile(reunite, "addNoiseWrap", fileName, type)


def writeOutfile(pathToOut, title, fileName, type):
	pathToOut.export("/Users/Capodit3/Documents/Sensedata/sense-os project2/noiseSound2/" + title + '_' + type + '_' + fileName, format='wav')

for fileName in hallway_onlyfiles:
    if not fileName == '.DS_Store':
		file2 = speech[counter]
		file2 = speechCorpus + '/' + file2
		file = hallway + '/' + fileName
		print file
		pathTosound1 = AudioSegment.from_wav(file)
		pathTosound2 = AudioSegment.from_wav(file2)
		print "adding noise from hallway to: " + file
		#addNoiseLater(pathTosound1, pathTosound2, fileName, "hallway")
		addNoiseFirst(pathTosound1, pathTosound2, fileName, "hallway")
		#addNoiseBetween(pathTosound1, pathTosound2, fileName, "hallway")
		#addNoiseWrap(pathTosound1, pathTosound2, fileName, "hallway")
		counter += 1
    
for fileName in office_onlyfiles:
    if not fileName == '.DS_Store':
		file2 = speech[counter]
		file2 = speechCorpus + '/' + file2
		file = office + '/' + fileName
		pathTosound1 = AudioSegment.from_wav(file)
		pathTosound2 = AudioSegment.from_wav(file2)
		print "adding noise from office to: " + file
		#addNoiseLater(pathTosound1, pathTosound2, fileName, "office")
		addNoiseFirst(pathTosound1, pathTosound2, fileName, "office")
		#addNoiseBetween(pathTosound1, pathTosound2, fileName, "office")
		#addNoiseWrap(pathTosound1, pathTosound2, fileName, "office")
		counter += 1
    
for fileName in park_onlyfiles:
    if not fileName == '.DS_Store':
		file2 = speech[counter]
		file2 = speechCorpus + '/' + file2
		file = park + '/' + fileName
		pathTosound1 = AudioSegment.from_wav(file)
		pathTosound2 = AudioSegment.from_wav(file2)
		print "adding noise from park to: " + file
		#addNoiseLater(pathTosound1, pathTosound2, fileName, "park")
		addNoiseFirst(pathTosound1, pathTosound2, fileName, "park")
		#addNoiseBetween(pathTosound1, pathTosound2, fileName, "park")
		#addNoiseWrap(pathTosound1, pathTosound2, fileName, "park")
		counter += 1

'''
addNoiseWrap(sound1, sound2)
'''
