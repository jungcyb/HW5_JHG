import csv

def main() :
	f = open('q2.csv', 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	header = next(data)

	mx_same = []
	mx_diff = -1

	mn_same = []
	mn_diff = 999999

	# 0: '날짜', 1: '지점', 2: '평균기온(℃)', 3: '최저기온(℃)', 4: '최고기온(℃)'
	for row in data :
		if(row[3] == '' or row[4] == '' or row[2] == '') : continue
		row[3], row[4], row[2] = float(row[3]), float(row[4]), float(row[2])
		
		diff = row[4] - row[3]
		
		if(mx_diff < diff) :
			mx_diff = diff
			mx_same = []
			mx_same.append(row[0])
		elif(mx_diff == diff) :
			mx_same.append(row[0])
		
		if(mn_diff > diff) :
			mn_diff = diff
			mn_same = []
			mn_same.append(row[0])
		elif(mn_diff == diff) :
			mn_same.append(row[0])

	print("*** Annual Temperature Report for Seoul in 2022 ***")
	for day in mx_same :
		print(f"Day with the Largest Temperature Variation: {day}")
	print(f"Maximum Temperature Difference: {round(mx_diff, 2):.2f} Celsius")

	for day in mn_same :
		print(f"Day with the Smallest Temperature Variation: {day}")
	print(f"Minimum Temperature Difference: {round(mn_diff, 2):.2f} Celsius")



	f.close()

if __name__ == "__main__" :
	main()