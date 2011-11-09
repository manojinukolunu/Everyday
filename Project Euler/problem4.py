def isPalindrome(n):
    list1=findPalindrome(n)
    list2=[]
    list3=[]
    for i in range(len(list1)/2):
        list2.append(list1[i])
    for i in range(len(list1)/2,len(list1)):
        list3.append(list1[i])
   # print list2
    list3.reverse()
    return list3==list2
    #print list3==list2
    
def findPalindrome(n):
    b=str(n)
    c=[]
    for i in b:
        c.append(int(i))
    return c



palindrome=[]
for i in range(100,1000):
    for j in range(100,1000):
        if isPalindrome(i*j):
            palindrome.append(i*j)

print max(palindrome)
