import csv
import pandas
field=['name','age','roll no']
sdict=[{'name':"anuarg",'age':22,'roll no':16},{'name':"aparna",'age':22,'roll no':17}]



with open("dpt.csv",'w')as dfile:
	writer=csv.DictWriter(dfile,fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)
data=pandas.read_csv("dpt.csv")
print(data)

