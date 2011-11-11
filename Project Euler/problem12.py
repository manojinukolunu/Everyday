
def generateTriangle(i):
	return i*(i+1)/2
def countDivisors(num):
	count=0
	i=1
	while True:
		if num%i==0:
			count=count+1
		if i>num/2:
			break
		i=i+1
	return count+1
i=100
while True:
	n=generateTriangle(i)
	count=countDivisors(n)
	print count
	if count>500:
		print n
		break
	i=i+1
