import csv

#csv1 = open('mfccJos.csv', 'rb')
csv2 = open('vad_features.csv', 'rb')
csvTo = open('vadMfccTotal.csv', 'wb')
br = "\n"

count = 1

for row in csv2.readlines():
	str = ""
	value = row.split(';')
	if  'filename' == 'filename':
		csv1 = open('melsfeat.csv', 'rb')
		for row2 in csv1.readlines():
			value2 = row2.split(';')
			value2b = value2[14].split('\n')[0]
			
			if value[0] == 'filename' and value2b == 'filename':
				str = value2b+';'+value2[0]+';'+ value[4].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]

#				csvTo.write(str)
#				csvTo.write('\n')

			if value[0] == value2b and not value[0] == 'filename' and count == 1:
				#print value[0], value2
				str = value2b+';'+value2[0]+';'+ value[4].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]
                count = 0
                print value
#csvTo.write(str)
#				csvTo.write('\n')
		csv1.close()

csvTo.close()

