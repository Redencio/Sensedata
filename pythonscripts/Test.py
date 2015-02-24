import os
from os import listdir
from os.path import isfile, join

rawPath  = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/audiofiles/splitted' 

noisePath  = '/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/audiofiles/splitted' 

onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]

/*

For each file in rawpath
	add noise
		from noisePath
*/

