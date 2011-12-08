def sumrec(seq,i):
    if i==len(seq):
        return 0
    elif i+1<=len(seq):
        return seq[i]+sumrec(seq[i+1:],i)

print sumrec(range(1,125),0)
