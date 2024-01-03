slist=open("stud.txt",'r')
olist=open("odd.txt",'w')
elist=open("even.txt",'w')

contents=slist.readlines()
print(contents)

for i in range(len(contents)):
	if(i%2==0):
		elist.write(contents[i])
	else:
		olist.write(contents[i])
slist.close()
olist.close()
elsit.close()
