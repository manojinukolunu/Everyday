def ins_sort_rec(seq,i):
    if i==0:
        return
    ins_sort_rec(seq,i-1)
    print str(i)+"\n"
    j=i
    print j
    while j>0 and seq[j-1]>seq[j]:
        seq[j-1],seq[j]=seq[j],seq[j-1]
        j-=1


list1=[4,1,2,3]
ins_sort_rec(list1,3)
print list1
