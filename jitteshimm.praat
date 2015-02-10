samples_directory$ = "/Volumes/LstarR HDD/Redencio2013-2014/noise_sec"
Create Table with column names... vectors 23 pitch1 pitch2 jitt1 jitt2 jitt3 jitt4 jitt5 shim1 shim2 shim3 shim4 shim5 shim6
Create Strings as file list... fileList 'samples_directory$'*.wav
numberOfFiles = Get number of strings
seperatot$ = ","
for i to numberOfFiles
select Strings fileList
fileName$ = Get string... i
sex$ = right$(fileName$,5)
Read from file... 'samples_directory$''fileName$'
currentSound$ = selected$ ("Sound")
   if sex$ == "M.wav"
    pitchFloor = 75
    pitchCealing = 300
    To Pitch (cc)... 0 pitchFloor 15 no 0.03 0.45
    ...0.01 0.35 0.14 pitchCealing
    startTime = Get starting time
    endTime = Get finishing time
   elsif sex$ == "F.wav"
    pitchFloor = 100
    pitchCealing = 500
    To Pitch (cc)... 0 pitchFloor 15 no 0.03 0.45
    ...0.01 0.35 0.14 pitchCealing
    startTime = Get starting time
    endTime = Get finishing time
   endif
select Sound 'currentSound$'
plus Pitch 'currentSound$'
To PointProcess (cc)
select Sound 'currentSound$'
plus Pitch 'currentSound$'
plus PointProcess 'currentSound$'
speechAnalysis$ = Voice report... startTime endTime pitchFloor
pitchCealing 1.3 1.6 0.03 0.45
pitchMean = extractNumber (speechAnalysis$, "Mean pitch: ")
pitchSD =extractNumber (speechAnalysis$, "Standard deviation: ")
jitterLocal = extractNumber (speechAnalysis$, "Jitter (local): ")
jitterLocalAbsol = extractNumber (speechAnalysis$, "Jitter (local,
absolute): ")
jitterRap = extractNumber (speechAnalysis$, "Jitter (rap): ")
jitterPPQ5 = extractNumber (speechAnalysis$, "Jitter (ppq5): ")
jitterDDP = extractNumber (speechAnalysis$, "Jitter (ddp): ")
shimmerLocal = extractNumber (speechAnalysis$, "Shimmer (local): ")
shimmerLocalDB = extractNumber (speechAnalysis$, "Shimmer (local, dB):
")
shimmerAPQ3 = extractNumber (speechAnalysis$, "Shimmer (apq3): ")
shimmerAPQ5 = extractNumber (speechAnalysis$, "Shimmer (apq5): ")
shimmerAPQ11 = extractNumber (speechAnalysis$, "Shimmer (apq11): ")
shimmerDDA = extractNumber (speechAnalysis$, "Shimmer (dda): ")
select Table vectors
Set numeric value... i pitch1 pitchMean
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
endfor
select Table vectors
Write to table file... /Volumes/LstarR HDD/Redencio2013-2014/noise_sec/outputvectors.xls