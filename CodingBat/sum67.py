def sum67(nums):
    sum=0
    i=0
   # print sum
    while i<len(nums):
        if nums[i]==6:
            #print i
            for j in range(i,len(nums)):
                if nums[j]==7:
                    i=j+1
                    
                    break
        else:
            sum=sum+nums[i]
            i=i+1
    return sum

print sum67([2, 2, 6, 7, 7])
