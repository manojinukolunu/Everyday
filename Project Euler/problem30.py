def findnum(n):
    sum1=0
    for i in str(n):
        sum1=sum1+(int(i)**5)
    if str(sum1)==str(n):
        return True
    else:
        return False

n=1
sum2=0
while True:
    if findnum(n):
        print n
        sum2=sum2+n
        print "sum : "+str(sum2-1)
    n+=1
