def counting(A,k):
    C=(k+1)*[0]
    B=(len(A)+1)*[0]
    for j in range(len(C)):
        C[j]=A.count(j)
    for j in range(1,len(C)):
        C[j]=C[j]+C[j-1]
    for j in range(len(A)-1,-1,-1):
        print "j="+str(j)+" A[j]="+str(A[j])+" C[A[j]]="+str(C[A[j]])
        B[C[A[j]]]=A[j]
        C[A[j]]=C[A[j]]-1
    return B[1:]

A=[6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2]
print counting(A,6)
