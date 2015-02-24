import csv

#csv1 = open('mfccJos.csv', 'rb')
csv2 = open('vad1a+b.csv', 'rb')
csv2 = open('jittShimm.csv', 'rb')
csvTo = open('jshMfccTotalab.csv', 'wb')
br = "\n"

count = 1
'''
for row in csv2.readlines():
	str = ""
	value = row.split(';')
	if  'filename' == 'filename':
		csv1 = open('mel1a+b.csv', 'rb')
		for row2 in csv1.readlines():
			value2 = row2.split(';')
			value2b = value2[14].split('\n')[0]
			
			if value[0] == 'filename' and value2b == 'filename':
				str = value2b+';'+value2[0]+';'+ value[4].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]
				print ''
				csvTo.write(str)
				csvTo.write('\n')

			if value[0] == value2b and not value[0] == 'filename':
				#print value[0], value2
				str = value2b+';'+value2[0]+';'+ value[4].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]
                count = 0
                csvTo.write(str)
                csvTo.write('\n')
		csv1.close()

'''

for row in csv2.readlines():
	str = ""
	value = row.split(';')
	if  'filename' == 'filename':
		csv1 = open('mel1a+b.csv', 'rb')
		for row2 in csv1.readlines():
			value2 = row2.split(';')
			value2b = value2[14].split('\n')[0]

			valueb = value[14].split('\n')[0]
			if valueb == 'filename' and value2b == 'filename':
				str = value2b+';'+value2[0]+';'+ value[0].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]+';'+ value[4]+';'+ value[5]+';'+ value[6]+';'+ value[7]+';'+ value[8]+';'+value[9]+	';'+ value[10]+';'+ value[11]+';'+ value[12]+';'+ value[13]
				print '', str
				print valueb, value2b
				csvTo.write(str)
				csvTo.write('\n')

			if valueb == value2b and not valueb == 'filename':
				#print value[0], value2
				str = value2b+';'+value2[0]+';'+ value[0].split('\r\n')[0]+';'+ value2[1]+';'+ value2[2]+';'+ value2[3]+';'+ value2[4]+';'+ value2[5]+';'+ value2[6]+';'+ value2[7]+';'+ value2[8]+';'+ value2[9]+';'+ value2[10]+';'+ value2[11]+';'+ value2[12]+';'+ value2[13]+';'+ value[1]+';'+ value[2]+';'+ value[3]+';'+ value[4]+';'+ value[5]+';'+ value[6]+';'+ value[7]+';'+ value[8]+';'+value[9]+	';'+ value[10]+';'+ value[11]+';'+ value[12]+';'+ value[13]
                count = 0
                #break
                csvTo.write(str)
                csvTo.write('\n')
		csv1.close()
csvTo.close()

