def round_sum(a,b,c):
    return round10(a)+round10(b)+round10(c)


def round10(num):
    num=str(num)
    if int(num[len(num)-1])<5:
        return int(num)-int(num[len(num)-1])
    if int(num[len(num)-1])>=5:
        return int(num)+10-int(num[len(num)-1])

print round_sum(6,4,4)
