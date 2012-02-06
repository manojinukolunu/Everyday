def sumdiag(table):
    sum1=0
    sum2=0
    table1=[]
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i==j:
                sum1=sum1+table[i][j]
    for i in table:
        i.reverse()
    
    for i in range(len(table)):
        for j in range(len(table[i])):
            if i==j:
                sum2=sum2+table[i][j]
    return sum1+sum2-1

k=1001
table= [ [ 0 for i in range(k) ] for j in range(k) ]
center=k/2
row=center
column=center
i=1
table[row][column]=1
count=1
try:
    while(True):
        #moving right 
        column=column+i
        count=count+i
        table[row][column]=count
        #moving down 
        row=row+(2*i)-1
        count=count+(2*i)-1
        table[row][column]=count
        #moving left 
        column=column-(2*i)
        count=count+(2*i)
        table[row][column]=count
        #moving up
        row=row-(2*i)
        count=count+(2*i)
        table[row][column]=count
        #moving right
        column=column+i
        count=count+i
        table[row][column]=count
        table[row][column+i]=count+i
        i+=1
except:
    print sumdiag(table)
    
    
