list1=[0,0,2,0,6,3,1,6,3,1]
tortoise=list1[0]
hare=list1[0]
i=0
while True:
    if hare==list1[-1]:
        print "No loop Found"
        break
    i=i+1
    if i<len(list1):
        print i
        hare=list1[i]
    if hare==list1[-1]:
        print "No loop Found"
        break
    i=i+1
    if i<len(list1):
        hare=list1[i]
    if i-1>=0 and i-1<len(list1):
        print i
        tortoise=list1[i-1]

    if hare==tortoise:
        print "Loop Found"
        break
