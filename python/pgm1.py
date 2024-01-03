with open("stud.txt")as f:
	slist=f.readlines()
print(slist)
slist=[x.strip() for x in slist]
print("the contents of file are")
print(slist)
