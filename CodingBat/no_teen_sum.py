def no_teen_sum(a, b, c):
  if a not in range(13,20) and b not in range(13,20) and c not in range(13,20):
    return (a+b+c)
  else:
    sum1=fix_teen(a)
    sum2=fix_teen(b)
    sum3=fix_teen(c)
    return (sum1+sum2+sum3)

def fix_teen(n):
  if n in range(13,20):
    if n==15 or n==16:
      return int(n)
    else :
      return int(0)
  else :
      return n

print no_teen_sum(2,1,14)
