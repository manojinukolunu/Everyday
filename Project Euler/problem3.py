import math
def factorize(n):
    factors=[]
    for i in range(2,int(math.sqrt(n))):
        while (n%i==0):
            factors.append(i)
            n=n/i
    return factors

print factorize(600851475143)
