import csv

def main() :
	f = open('q3.csv', 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	usages = [[0, i] for i in range(0, 10)]

	# 0: 사용월, 1:호선명, 2:역ID, 3:지하철역, 4:승차승객수,5:하차승객수,6:작업일시

	header = next(data)
	for row in data :
		if(row[5] == '' or row[4] == '') : continue
		row[5], row[4] = int(row[5]), int(row[4])
		
		try :
			usage = row[4] + row[5]
			line = int(row[1][0:1])
			usages[line][0] += usage
		except Exception :
			continue

	usages.sort()

	print("*** Subway Report for Seoul on March 2023 ***")
	print(f"1st Busiest Line: Line {usages[9][1]} ({usages[9][0]})")
	print(f"2nd Busiest Line: Line {usages[8][1]} ({usages[8][0]})")

	print(f"1st Least used Line: Line {usages[1][1]} ({usages[1][0]})")
	print(f"2nd Least used Line: Line {usages[2][1]} ({usages[2][0]})")

	f.close()

if __name__ == "__main__" :
	main()