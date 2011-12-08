A=[31,41,59,26,41,58]
for j in range(1,len(A)):
  key=A[j]
  for i in range(0,j):
    if A[i]>A[j]:
      A[i],A[j]=A[j],A[i]
      print A
  print A


