def fib(n):
    a=1
    b=1
    i=3
    while(i<=n):
        c=a+b
        a=b
        b=c
        i=i+1
    return a    
sum=0
for i in range(3,4000000):
    if fib(i)<4000000:
        #print fib(i)%2
        if fib(i)%2==0:
            sum=sum+fib(i)
    else:
        break
print sum
