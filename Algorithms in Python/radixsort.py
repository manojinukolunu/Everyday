def radixSort(seq):
    seq1=[]
    for i in range(len(seq)):
        seq1.append(seq[i]%10)
        seq[i]=seq[i]/10
    return seq1,seq

print radixSort([423,221,334,112])
