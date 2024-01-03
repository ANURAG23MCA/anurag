import csv
with open("st.csv",'r')as efile:
	data=csv.reader(efile)
	for i in data:
		print(i)
