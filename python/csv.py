import csv
limport csv
import pandas
field=['empno','name','dept']
sdict=[{'empno':"101",'name':"Anu",'dept':"MCA"},{'empno':"102",'name':"Anna",'dept':"MCA"}
with open("dep.csv",'w')as dfile:
	writer=csv.DictWriter(dfile,fieldnames=field)
	writer.writeheader()
	writer.writerows(sdict)
data=pandas.read_csv("dep.csv")
print(data)

	
