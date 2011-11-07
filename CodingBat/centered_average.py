def centered_average(nums):
    sum=0
    nums.sort()
    for i in range(len(nums)):
        if i==0 or i==len(nums)-1:
            pass
        else:
            sum=sum+nums[i]
    return sum/(len(nums)-2)
print centered_average([5,3,4,0,100])
    
