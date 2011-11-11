f=open('file.txt','r')
list1=f.readlines()
for i in range(len(list1)):
	list1[i]=int(list1[i].replace("\n",""))
sum=0
for i in list1:
	sum=sum+i
print sum
5537376230390876637302048746832985971773659831892672

