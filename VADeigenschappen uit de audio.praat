form Read multiple files
	sentence source_directory /Volumes/LstarR HDD/Redencio2013-2014/josSpeech/
	#sentence source_directory /Users/Capodit3/Documents/Sensedata/sense-os project2/noiseSound/
	sentence file_extension .mp3
endform
#/Volumes/LstarR HDD/Redencio2013-2014/sense - audio/speechCorpus/
Create Strings as file list... list 'source_directory$'/*'file_extension$'
Sort

string_ID = selected("Strings")
number_of_files = Get number of strings
printline file_name;total_energy;total_F;total_SFM;speech;

for ifile to number_of_files 
	select Strings list
	file_name$ = Get string... ifile
	audio$ = Read from file... 'source_directory$'/'file_name$'
	
	object_name$  = replace_regex$ (file_name$, ".mp3", "", 0)
	object_name$  = replace_regex$ (object_name$, " ", "_", 0)
	select Sound 'object_name$'
	
	start_frequency = 300
	end_frequency = 10000


	total_energy = 0
	total_F = 0
	total_SFM = 0
	aantal = 0
	number_of_steps = 0

	sound_id = selected("Sound")
	sound_name$ = selected$("Sound")

	sampling_period = Get sampling period


	sum_wiener_entropy = 0

	## Energy ##
	To Intensity... 100 0.064 1
	intensity_id = selected("Intensity")
	energy = Get mean... 0.0 0.0 dB
	#printline energy: 'energy'
		
	total_energy += energy
	##End Energy##
		
	select Sound 'object_name$'
	duration = Get total duration
	start_time = Get starting time

	sum_wiener_entropy = 0
		
	To Spectrum (dft)
	spectrum_id = selected("Spectrum")
	Rename... Spectrum
	number_of_bins = Get number of bins
	highest_frequency = Get highest frequency

	if highest_frequency < end_frequency
			end_frequency = highest_frequency
	endif

	start_bin = Get bin number from frequency... 'start_frequency'
	end_bin = Get bin number from frequency... 'end_frequency'
	start_bin = round(start_bin)
	end_bin = round(end_bin)
	actual_start_frequency = Get frequency from bin number... 'start_bin'
	actual_end_frequency = Get frequency from bin number... 'end_bin'
	number_of_band_bins = end_bin - start_bin + 1
	Create simple Matrix... power_spectrum 1 'number_of_band_bins' 0
	power_spectrum_id = selected("Matrix")
	Formula... ((Spectrum_Spectrum [1,col]/sampling_period)^2 + (Spectrum_Spectrum [2,col]/sampling_period)^2)

	hoogste_bin = start_bin
	hoogste_spectrum = 0
	sum_power_spectrum = 0
	for bin from start_bin to end_bin
		mps = Matrix_power_spectrum[1,bin]
		sum_power_spectrum += mps
		if hoogste_spectrum < mps
			hoogste_bin = bin
			hoogste_spectrum = sum_power_spectrum
		endif
	endfor
	
	select spectrum_id
	actual_dominant_frequency = Get frequency from bin number... 'hoogste_bin'
	total_F += actual_dominant_frequency
	#printline dfc 'actual_dominant_frequency'
		arithmetic_mean = sum_power_spectrum/number_of_bins
		Create simple Matrix... ln_power_spectrum 1 'number_of_band_bins' 0
	ln_power_spectrum_id = selected("Matrix")
	Formula... ln(Matrix_power_spectrum[])
		sum_ln_power_spectrum = 0
	for bin from start_bin to end_bin
		sum_ln_power_spectrum += Matrix_ln_power_spectrum[1,bin]
	endfor
	geometric_mean = exp(sum_ln_power_spectrum/number_of_band_bins)
		frame_wiener_entropy = ln(geometric_mean/arithmetic_mean)
	#printline wiener entropy frame 'frame_no': 'frame_wiener_entropy'
	if frame_wiener_entropy = undefined
		number_of_steps -= 1
	else
		sum_wiener_entropy += frame_wiener_entropy
	endif
	select 'spectrum_id'
	plus 'power_spectrum_id'	
	plus 'ln_power_spectrum_id'
	#plus 'sound_frame_id'
	Remove
	#select 'sound_id'
	
	wiener_entropy = sum_wiener_entropy
	#printline mean wiener entropy: 'wiener_entropy'
	total_SFM = wiener_entropy

	#uitprinten resultaten
	printline 'file_name$';'total_energy';'total_F';'total_SFM';1;

endfor

select 'string_ID'

Remove