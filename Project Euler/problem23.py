def findAbundant():
    f=open("abundant.txt",'r')
    list1=[]
    for i in f.readlines():
        list1.append(i.replace("\n","").split(" "))
    sum=0
    for i,j in list1:
        if j!='':
            sum=sum+int(j)
    return sum
    
print findAbundant()
