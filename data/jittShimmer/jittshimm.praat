#form Read all files of the given type from the given directory
   sentence Source_directory /Volumes/LstarR HDD/Redencio2013-2014/noise_sec2
   sentence File_name_or_initial_substring 
   sentence File_extension .wav
#endform
Create Strings as file list... list 'source_directory$'/'file_name_or_initial_substring$'*'file_extension$'
head_words = selected("Strings")
file_count = Get number of strings
for ifile to file_count
   select Strings list
   filename$ = Get string... ifile
   Read from file... 'source_directory$'/'filename$'
name$ = selected$("Sound",1)
 minimum_pitch = 70
 maximum_pitch = 625
 
 pitch_silence_threshold = 0.03
 pitch_voicing_threshold = 0.45
 pitch_octave_cost = 0.01
 pitch_octave_jump_cost = 0.35
 pitch_voiced_unvoiced_cost = 0.14
maximum_period_factor = 2
maximum_amplitude_factor = 9
To Pitch (ac)... 0 minimum_pitch 15 no pitch_silence_threshold pitch_voicing_threshold 
 ...0.01 0.35 0.14 maximum_pitch

plus Pitch 'name$'
 
To PointProcess
points = Get number of points
#Remove
 
select Sound 'name$'
plus Pitch 'name$'
plus PointProcess 'name$'
#Voice report... start end minimum_pitch maximum_pitch maximum_period_factor
maximum_amplitude_factor 0.03 0.45
report$ = Voice report... start end minimum_pitch maximum_pitch maximum_period_factor
maximum_amplitude_factor 0.03 0.45

medianPitch = extractNumber (report$, "Median pitch: ")
meanPitch = extractNumber (report$, "Mean pitch: ")
sdPitch =extractNumber (report$, "Standard deviation: ")
minPitch = extractNumber (report$, "Minimum pitch: ")
maxPitch = extractNumber (report$, "Maximum pitch: ")

jitter_loc = extractNumber (report$, "Jitter (local): ") * 100
jitter_loc_abs = extractNumber (report$, "Jitter (local, absolute): ") * 1000000
jitter_rap = extractNumber (report$, "Jitter (rap): ") * 100
jitter_ppq5 = extractNumber (report$, "Jitter (ppq5): ") *100
shimmer_loc = extractNumber (report$, "Shimmer (local): ") *100
shimmer_loc_dB = extractNumber (report$, "Shimmer (local, dB): ")
shimmer_apq3 = extractNumber (report$, "Shimmer (apq3): ") * 100
shimmer_apq5 = extractNumber (report$, "Shimmer (apq5): ") * 100
shimmer_apq11 = extractNumber (report$, "Shimmer (apq11): ") * 100
mean_nhr = extractNumber (report$, "Mean noise-to-harmonics ratio: ")
min_intensity = extractNumber (report$, "minimum intensity: ")

fileappend "'save_directory$'\'user_specified_file_name$'" 
 ...'tab$''medianPitch''tab$''meanPitch''tab$''sdPitch''tab$''minPitch''tab$''maxPitch'
 ...'tab$''jitter_loc''tab$''jitter_loc_abs''tab$''jitter_rap''tab$''jitter_ppq5''tab$'
 ...'shimmer_loc''tab$''shimmer_loc_dB''tab$''shimmer_apq3''tab$''shimmer_apq5''tab$''shimmer_apq11'
 ...'tab$''mean_nhr''tab$''newline$'

select Pitch 'name$'
Remove
select PointProcess 'name$'
Remove
select Sound 'name$'

endfor