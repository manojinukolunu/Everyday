
def calcSum(string,pos):
    sum=0
    for i in string:
        sum=sum+(ord(i)-64)
    return sum*pos
    

def readLines():
    f=open("names.txt",'r')
    list1=f.read().replace("\"","").split(",")
    list1.sort()
    print len(list1)
    sum=0
    for i in list1:
        sum=sum+calcSum(i,list1.index(i)+1)
    f.close()
    return sum

print readLines()
