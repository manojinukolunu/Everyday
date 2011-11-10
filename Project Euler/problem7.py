import math
def testPrime(num):
    i=2
    while i<=math.sqrt(num):
        if num%i==0:
            return False
        i=i+1
    return True

def genPrimes():
    sum1=0
    i=1
    prime=False
    count=1
    while True:
        num=2*i+1
        if testPrime(num) and num<2000000:
            sum1=sum1+num
            count=count+1
        elif num>=2000000:
            break
        i=i+1
    return sum1

print genPrimes()+2
