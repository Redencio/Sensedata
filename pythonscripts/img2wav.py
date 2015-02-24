import wave

try:
    #change the file's name and format
    image_file = 'image.jpg'
    fin = open(image_file, "rb") #binary read
    data = fin.read()
    fin.close()
except IOError:
    print("Image file %s not found" % imageFile)
    raise SystemExit

#Give the name for wav file produced at run time corresponding to the input file
sound_output = wave.open('image.wav', 'w')
sound_output.setparams((1, 2, 44100, 10, 'NONE', 'not compressed'))

hex_str = bytes(data) #convert binary data to string of bytes
sound_output.writeframes(hex_str)


sound_output.close()