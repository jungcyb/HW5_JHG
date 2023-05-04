import csv

def main() :
	f = open('q1.csv', 'r', encoding='cp949')
	data = csv.reader(f, delimiter=',')

	cnt = 0
	avg_temp = 0
	min_temp = 0
	mx_temp = 0

	header = next(data)
	# 0: '날짜', 1: '지점', 2: '평균기온(℃)', 3: '최저기온(℃)', 4: '최고기온(℃)'
	for row in data :
		if(row[3] == '' or row[4] == '' or row[2] == '') : continue
		row[3], row[4], row[2] = float(row[3]), float(row[4]), float(row[2])
		cnt += 1
		avg_temp += row[2]
		min_temp += row[3]
		mx_temp += row[4]

	print("*** Annual Temperature Report for Seoul in 2022 ***")
	print(f"Average Temperature: {round(avg_temp / cnt, 2):.2f} Celsius")
	print(f"Average Minimum Temperature: {round(min_temp / cnt, 2):.2f} Celsius")
	print(f"Average Maximum Temperature: {round(mx_temp / cnt, 2):.2f} Celsius")

	f.close()

if __name__ == "__main__" :
	main()