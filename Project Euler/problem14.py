def sequence(n):
	count=0
	while n!=1:
		if n%2==0:
			n=n/2
			count=count+1
		else:
			n=3*n+1
			count=count+1
	return count+1
n=13
seqNumbers=[]

while n<1000000:
	seqNumbers.append(str(sequence(n))+" "+str(n))
	n=n+1

for i in seqNumbers:
	if i.startswith("525"):
		print i
