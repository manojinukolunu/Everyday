def findDivisor(n):
    list1=[]
    for i in range(1,n):
        if n%i==0:
            list1.append(i)
    return list1

def sumDivisors(n):
    return sum(findDivisor(n))


def sumAmicable(n):
    list1=[]
    for i in range(1,n+1):
        if i==sumDivisors(sumDivisors(i)) and i!=sumDivisors(i):
            list1.append(i)
    return list1
print sum(sumAmicable(10000))
