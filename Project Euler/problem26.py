def longdiv(dividend,divisor):
    quotient=0
    if remainder==0:
        return quotient
    else:
        if divisor<dividend:
            return longdiv(dividend%divisor,divisor)

print longdiv(11,7)

