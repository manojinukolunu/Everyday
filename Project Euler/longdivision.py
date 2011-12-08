def longdiv(divisor,dividend):
    #multiplying dividend by 10 to make it larger than divisor
    if divisor==dividend:
        return "1"
    if divisor>dividend:
        quotient="0."
        count10s=0
        while True:
            if dividend>=divisor:
                break
            dividend*=10
            quotient+="0"
            count10s+=1
        quotient=quotient[:-1]
    remainder=None
    remainders=[]
    while True:
        countrs=0
        remainder=dividend%divisor
        if remainder in remainders:
            break
        else:
            remainders.append(remainder)
        quotient=quotient+str(dividend/divisor)
        if remainder==0 or remainder==1:
            break
        if remainder>divisor:
            dividend=remainder
        else:
            while True:
                if remainder>divisor:
                    break
                remainder*=10
                countrs+=1
            if countrs>count10s:
                quotient=quotient+(countrs-count10s)*"0"
            dividend=remainder
    return len(quotient)

count=longdiv(1,1)
lens=[]
for i in range(3,1000):
    lens.append([longdiv(i,1),i])
print max(lens)
