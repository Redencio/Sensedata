#samples_directory$ = "/Users/agentleman/Documents/audio10noise/"
samples_directory$ = "/Users/agentleman/Documents/Sensedata/audio10/"
Create Strings as file list... list 'samples_directory$'/*.wav
#Sort
string_ID = selected("Strings")
number_of_files = Get number of strings

Create Table with column names... vectors 'number_of_files' speechJ pitch1 pitch2 jitt1 jitt2 jitt3 jitt4 jitt5 shim1 shim2 shim3 shim4 shim5 shim6 filename
Create Strings as file list... fileList 'samples_directory$'*.wav
numberOfFiles = Get number of strings

# pitch_silence_threshold = 0.03
# pitch_voicing_threshold = 0.45
# pitch_octave_cost = 0.01
# pitch_octave_jump_cost = 0.35
# pitch_voiced_unvoiced_cost = 0.14
#maximum_period_factor = 2
#maximum_amplitude_factor = 9
#To Pitch (ac)... 0 minimum_pitch 15 no pitch_silence_threshold pitch_voicing_threshold 
# ...0.01 0.35 0.14 maximum_pitch

seperatot$ = ","
for i to numberOfFiles
clearinfo
	select Strings fileList
	fileName$ = Get string... i
	sex$ = right$(fileName$,5)
	Read from file... 'samples_directory$''fileName$'
	currentSound$ = selected$ ("Sound")
	#if sex$ == "M.wav"
	pitchFloor = 75
	pitchCealing = 300
	.pitch = To Pitch (cc)... 0 pitchFloor 15 no 0.03 0.45 0.01 0.35 0.14 pitchCealing
	##print '.pitch'
	startTime = Get starting time
	endTime = Get finishing time
	##print 'endTime'
#   elsif sex$ == "F.wav"
#   pitchFloor = 100
#    pitchCealing = 500
#    To Pitch (cc)... 0 pitchFloor 15 no 0.03 0.45
#    ...0.01 0.35 0.14 pitchCealing
#    startTime = Get starting time
#    endTime = Get finishing time
	#endif
	select Sound 'currentSound$'
	plus Pitch 'currentSound$'
	To PointProcess (cc)
	select Sound 'currentSound$'
	plus Pitch 'currentSound$'
	plus PointProcess 'currentSound$'_'currentSound$'
	speechAnalysis$ = Voice report... startTime endTime pitchFloor pitchCealing 1.3 1.6 0.03 0.45
	##print 'speechAnalysis$'
	pitchMean = extractNumber (speechAnalysis$, "Mean pitch:")
	pitchSD =extractNumber (speechAnalysis$, "Standard deviation:")
	jitterLocal = extractNumber (speechAnalysis$, "Jitter (local):")
	jitterLocalAbsol = extractNumber (speechAnalysis$, "Jitter (local, absolute):")
	jitterRap = extractNumber (speechAnalysis$, "Jitter (rap):") * 100
	jitterPPQ5 = extractNumber (speechAnalysis$, "Jitter (ppq5):")
	jitterDDP = extractNumber (speechAnalysis$, "Jitter (ddp): ")
	shimmerLocal = extractNumber (speechAnalysis$, "Shimmer (local):")
	shimmerLocalDB = extractNumber (speechAnalysis$, "Shimmer (local, dB):")
	shimmerAPQ3 = extractNumber (speechAnalysis$, "Shimmer (apq3):")
	shimmerAPQ5 = extractNumber (speechAnalysis$, "Shimmer (apq5):")
	shimmerAPQ11 = extractNumber (speechAnalysis$, "Shimmer (apq11):")
	shimmerDDA = extractNumber (speechAnalysis$, "Shimmer (dda):")

	if pitchMean == undefined
		pitchMean = 0
	endif
	if pitchSD == undefined
		pitchSD = 0
	endif		
	if jitterLocal == undefined
		jitterLocal = 0
	endif		
	if jitterLocalAbsol == undefined
		jitterLocalAbsol = 0
	endif		
	if jitterRap == undefined
		jitterRap = 0
	endif		
	if jitterPPQ5 == undefined
		jitterPPQ5 = 0
	endif		
	if jitterDDP == undefined
		jitterDDP = 0
	endif		
	if shimmerLocal == undefined
		shimmerLocal = 0
	endif		
	if shimmerLocalDB == undefined
		shimmerLocalDB = 0
	endif		
	if shimmerAPQ3 == undefined
		shimmerAPQ3 = 0
	endif		
	if shimmerAPQ5 == undefined
		shimmerAPQ5 = 0
	endif		
	if shimmerAPQ11 == undefined
		shimmerAPQ11 = 0
	endif
	if shimmerDDA == undefined
		shimmerDDA = 0
	endif		
	select Table vectors
	Set numeric value... i pitch1 pitchMean
	##print 'pitchMean'
	Set string value... i speechJ 1
	Set numeric value... i pitch2 pitchSD
	Set numeric value... i jitt1 jitterLocal
	Set numeric value... i jitt2 jitterLocalAbsol
	Set numeric value... i jitt3 jitterRap
	Set numeric value... i jitt4 jitterPPQ5
	Set numeric value... i jitt5 jitterDDP
	Set numeric value... i shim1 shimmerLocal
	Set numeric value... i shim2 shimmerLocalDB
	Set numeric value... i shim3 shimmerAPQ3
	Set numeric value... i shim4 shimmerAPQ5
	Set numeric value... i shim5 shimmerAPQ11
	Set numeric value... i shim6 shimmerDDA
	Set string value... i filename 'currentSound$'

	select Table vectors
	#Write to table file... /Users/agentleman/Documents/Sensedata/jittShimmNoise-audio10.csv
	Write to table file... /Users/agentleman/Documents/Sensedata/jittShimmSpeech-audio10.csv
endfor
