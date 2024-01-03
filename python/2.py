n=int(input("Enter number of elements : "))
a=[]
for i in range(n):
 e=int(input())
 a.append(e)
m=min(a)
x=max(a)
a.append(10)
a= list(dict.fromkeys(a))
print("smallest:",m)
print("largest:",x)
print(a)
