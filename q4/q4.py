import csv

def main() :
	f = open('q4.csv', 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	dct = dict()

	mx_usages = [[0, ''] for _ in range(0, 10)]
	mn_usages = [[999999999999, ''] for _ in range(0, 10)]
	# 0: 사용월, 1:호선명, 2:역ID, 3:지하철역, 4:승차승객수,5:하차승객수,6:작업일시
	header = next(data)
	for row in data :
		if(row[5] == '' or row[4] == '') : continue
		row[5], row[4] = int(row[5]), int(row[4])
		
		try :
			usage = row[4] + row[5]
			line = int(row[1][0:1])

			if(dct.get(row[3]) is None) :
				dct[row[3]] = 0

			dct[row[3]] = dct[row[3]] + usage

			if(mx_usages[line][0] < dct.get(row[3])) :
				mx_usages[line][0] = dct.get(row[3])
				mx_usages[line][1] = row[3]
			
			if(mn_usages[line][0] > dct.get(row[3])) :
				mn_usages[line][0] = dct.get(row[3])
				mn_usages[line][1] = row[3]
				
		except Exception :
			continue

	print("*** Subway Report for Seoul on March 2023 ***")
	for i in range(1, 5) :
		print("Line", i)
		print(f"Busiest Station: {mx_usages[i][1]} ({mx_usages[i][0]})")
		print(f"Least used Station: {mn_usages[i][1]} ({mn_usages[i][0]})")
	f.close()

if __name__ == "__main__" :
	main()