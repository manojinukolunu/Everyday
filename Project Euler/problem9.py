def findPythagoreanTriplet(num):
    for i in range(num):
        for j in range(num):
            if i**2+j**2==(1000-i-j)**2:
                if i!=0 and j!=0:
                    a=i
                    b=j
                    c=1000-a-b
                    product=a*b*c
    return product
        
print findPythagoreanTriplet(10001)
