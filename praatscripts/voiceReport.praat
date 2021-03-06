select Sound
masterSound = selected("Sound")
masterSound = selected("Sound")
call setupVoiceTable
call voiceReport masterSound setupVoice.voiceTable

############### get voice report ###############
procedure sound.voiceTable

#call voiceprint 'masterSound'
#procedure sound
select .sound
.masterIntensity = To Intensity… 100 0 yes
.contentTextGrid = To TextGrid(silences)… -25 0.1 0.05 silent sounding
plus .sound
Extract intervals where… 1 yes "is equal to" sounding

for .i from 1 to .nSel
	#.nSel = numberOfselected("Sound", i)
	extracted'.i' = = selected("Sound", i)
endfor

for .i from 1 to .nSel
	select extracted '.i'
	.masterPitch = To Pitch (ac)… 0.75 15 yes 0.03 0.45 0.01 0.35 0.14 600
	.meanPitch = Get mean… 0.0 Hertz
	.sdPitch = Get standard deviation… 0.0 Hertz
	.slopePitchHertz = Get mean absolute slope… Hertz
	.slopePitchERB = Get mean absolute slope… ERB
	.minPitch = Get minimum… 0.0 Hertz Parabolic
	.maxPitch = Get maximum… 0.0 Hertz Parabolic
	plus extracted'.i'
	.masterPoint = To PointProcess(cc)
	select extracted '.i'
	plus .masterPitch
	plus .masterPoint
	.masterVoices$ = Voice report.. 0 0 75 600 1.3 1.6 0.03 0.45
	.jitter = extractNumber(.masterVoice$, "Jitter(local):")
	.shimmer = extractNumber(.masterVoice$, "Shimmer(local):")
	.meanAuto = extractNumber(.masterVoice$, "Mean autocorrelation:")
	.meanNHR = extractNumber(.masterVoice$, "Mean noise-to-harmonics ratio:")
	.meanHTN = extractNumber(.masterVoice$, "Mean harmonics-to-noise ratio:")
	select = extracted'.i'
	plus .masterPoint
	.masterLtas = to Ltas… 4000 100 0.00001 0.02 1.3
	.ltasMean = Get mean… 0.0 energy
	.ltasSlope = Get slope… 0 1000 1000 4000 energy
	.ltasSd = Get standard deviation… 0 0 energy
	call exception
	call writeToVoiceTable setupVoiceTable.voiceTable setUpVoiceTable.rowNum '.meanPitch' '.sdPitch:2'
…'.slopePitchHertz''.slopePitchERB''.minPitch:2''.maxPitch:2''.jitter:2''.shimmer:2'
…'meanAuto:2''.meanNHR:2''.meanHTN:2'
…'.ltasMean:2''.ltasSlope:2''.ltasSd:2'
	setVoiceTable.RowNum += 1
	select extracted'.i'	
	plus .masterPitch
	plus .masterPoint
	plus .masterLtas
	plus .masterHarmonicity
	Remove
endfor
select .masterIntensity
plus .contentTextGrid
Remove
select .sound

select setupVoiceTable.voiceTable
.nRow = Get number of rows
.test = Get value….nrow unit

if.test == undefined
	Remove row….nrow
endif

############## exceptions #################
if meanPitch == undefined
	meanPitch = 0
if sdPitch == undefined
	sdPitch = 0
if slopePitchHertz == undefined
	slopePitchHertz = 0
if slopePitchERB == undefined
	slopePitchERB = 0
if minPitch == undefined
	minPitch = 0
if maxPitch == undefined
	 maxPitch = 0
if jitter == undefined
	jitter = 0
if shimmer == undefined
	shimmer = 0
if meanAuto == undefined
	meanAuto = 0
if meanNHR == undefined
	meanNHR = 0
if meanHTN == undefined
	meanHTN = 0
if ltasMean == undefined
	ltasMean = 0
if ltasSlope == undefined
	ltasSlope = 0
if ltasSd == undefined
	ltasSd = 0

################# set up table ###############
procedure setupVoiceTable
.rowNum = 1
.voiceTable = Create Table with column names… voiceTable 1 unit
… meanPitch sdPitch slopePitchHertz slopePitchERB minPitch maxPitch jitter shimmer meanAuto meanNHR meanHTN ltasMean ltasSlope ltasSd 
endproc

############### write to table ##################

procedure writeToVoiceTable.voiceTable .rowNum .meanPitch .sdPitch 
… .slopePitchHertz .slopePitchERB .minPitch .maxPitch .jitter .shimmer 
… .meanAuto .meanNHR .meanHTN .ltasMean .ltasSlope .ltasSd

select .VoiceTable

insert row… .rowNum
Set numeric value... .rowNum unit .rowNum
Set numeric value... .rowNum meanPitch .meanPitch
Set numeric value... .rowNum sdPitch .sdPitch
Set numeric value... .rowNum slopePitchHertz .slopePitchHertz
Set numeric value... .rowNum slopePitchERB .slopePitchERB
Set numeric value... .rowNum minPitch .minPitch
Set numeric value... .rowNum maxPitch .maxPitch
Set numeric value... .rowNum jitter .jitter
Set numeric value... .rowNum shimmer .shimmer
Set numeric value... .rowNum meanAuto .meanAuto
Set numeric value... .rowNum meanNHR .meanNHR
Set numeric value... .rowNum meanHTN .meanHTN
Set numeric value... .rowNum ltasMean .ltasMean
Set numeric value... .rowNum ltasSlope .ltasSlope
Set numeric value... .rowNum ltasSd .ltasSd
end proc
