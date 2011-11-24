'''Eulers Method for Finding The GCD of Two Numbers Algorithm from
The Art of Computer Programming Vol 1 by Knuth '''

def findGCD(m,n,count=0):
    if m<n:
        m,n=n,m
    r=m%n
    if r==0:
        return n,count
    else:
        m=n
        n=r
        count+=1
        return findGCD(m,n,count)
print findGCD(119, 544)
