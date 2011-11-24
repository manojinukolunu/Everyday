def dow(y,m,d):
    dict1={}
    dict1[0]="Sunday"
    dict1[1]="Monday"
    dict1[2]="Tuesday"
    dict1[3]="Wednesday"
    dict1[4]="Thursday"
    dict1[5]="Friday"
    dict1[6]="Saturday"
    
    list1=[0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    y-=m<3;
    return dict1[(y + y/4 - y/100 + y/400 + list1[m-1] + d) % 7]

print dow(1900,1,1)
count=0
for i in range(1901,2001):
    for j in range(1,13):
        if dow(i,j,1)=="Sunday":
            print j
            count+=1
print count
