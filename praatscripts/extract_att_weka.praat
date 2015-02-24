# ------------------------------------------------------------------
# Script Copyright by:
# Ignacio Alvarez 2012
# ignm@clemson.edu
# ------------------------------------------------------------------
# This Praat script processes an audio file on real-time 
# It generates the following attributes out of the audio analysis:
#	pitch: mean, max, min, sd
#	intensity: mean, max, min, sd
#	mfcc: mean
# Values are stored in variables and saved in an txt file.
# ------------------------------------------------------------------

#Read parameters from php and include them in the variables
#	form Write audio variables to file
#		word sound_path
#		word sound_name
#		word text_path	
#	endform


#clean info windows (only in Praats console)
#	clearinfo

# Delete the text file to include the newest values
#	filedelete 'text_path$'

# Read the audio file
#	Read from file... 'sound_path$''sound_name$'.wav


form Read multiple files
	sentence source_directory /Volumes/LstarR HDD/Redencio2013-2014/noise_sec/
	sentence file_extension .wav
endform
#/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/speechCorpus/
Create Strings as file list... list 'source_directory$'/*'file_extension$'
Sort

string_ID = selected("Strings")
number_of_files = Get number of strings


for ifile to number_of_files 

	select Strings list
	file_name$ = Get string... ifile
	audio$ = Read from file... 'source_directory$'/'file_name$'
	
	object_name$  = replace_regex$ (file_name$, ".wav", "", 0)
	object_name$  = replace_regex$ (object_name$, " ", "_", 0)
	select Sound 'object_name$'

	sound_id = selected("Sound")
	sound_name$ = selected$("Sound")

# Select audio, convert to pitch and get mean, min, max, sd
	select Sound 'sound_name$'
	To Pitch... 0 75 600
	select Pitch 'sound_name$'
	pitch = Get mean... 0 0 Hertz
	select Pitch 'sound_name$'
	min_pitch = Get minimum... 0 0 Hertz Parabolic
	select Pitch 'sound_name$'
	max_pitch = Get maximum... 0 0 Hertz Parabolic
	select Pitch 'sound_name$'
	sd_pitch = Get standard deviation... 0 0 Hertz


# Select audio, convert to intensity and get mean, min, max, sd
	select Sound 'sound_name$'
	To Intensity... 75 0 yes
	select Intensity 'sound_name$'
	intensity = Get mean... 0 0 energy
	select Intensity 'sound_name$'
	min_intensity = Get minimum... 0 0 Parabolic
	select Intensity 'sound_name$'
	max_intensity = Get maximum... 0 0 Parabolic
	select Intensity 'sound_name$'
	sd_intensity = Get standard deviation... 0 0

#Print values in Praat console
	printline 'pitch', 'sd_pitch', 'min_pitch', 'max_pitch', 'intensity', 'sd_intensity', 'min_intensity', 'max_intensity',
		
# Include Header in text file
	fileappend 'text_path$' @relation Emostate 'newline$' @attribute pitch numeric 'newline$' @attribute sd_pitch numeric 'newline$' @attribute min_pitch numeric 'newline$' @attribute max_pitch numeric 'newline$' @attribute intensity numeric 'newline$' @attribute sd_intensity numeric 'newline$' @attribute min_intensity numeric 'newline$' @attribute max_intensity numeric 'newline$' @attribute mean_c1 numeric 'newline$' @attribute mean_c2 numeric 'newline$' @attribute mean_c3 numeric 'newline$' @attribute mean_c4 numeric 'newline$' @attribute mean_c5 numeric 'newline$' @attribute mean_c6 numeric 'newline$' @attribute mean_c7 numeric 'newline$' @attribute mean_c8 numeric 'newline$' @attribute mean_c9 numeric 'newline$' @attribute mean_c10 numeric 'newline$' @attribute mean_c11 numeric 'newline$' @attribute mean_c12 numeric 'newline$' @data 'newline$'

# Save attribute values in text file 
	fileappend 'text_path$' 'pitch', 'sd_pitch', 'min_pitch', 'max_pitch', 'intensity', 'sd_intensity', 'min_intensity', 'max_intensity', 

#Get mean values for each MFCC C1-12 across the MFCC Matrix
	select Sound 'sound_name$'
	To MFCC... 12 0.5 0.05 100 100 0
	select MFCC 'sound_name$'
	To Matrix
	select Matrix 'sound_name$'
	#number of columns created which is the number of frames in which the audio lenght was divided we know there are 12 rows
	length = Get number of columns

	for cepstral from 1 to 12
		sum = 0
		#Extract the values for each row
					for c_value from 1 to 'length'
								   c'c_value' = Get value in cell... 'cepstral' 'c_value'
					endfor
		for j from 1 to 'length'
		sum += c'j'
		endfor
		mean'cepstral' = 'sum' / 'length'
		# We write the mean value in screen
		# We need a fillup variable
		foo = mean'cepstral'
		printline 'foo',
		# Save coefficients in text file
		fileappend 'text_path$' 'foo', 
	endfor

endfor

#select 'string_ID'

#Remove
	
# ------------------
# End of the script
# Ignacio Alvarez
# ------------------