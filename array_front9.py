def array_front9(nums):
    if len(nums)<=4:
        if (nums.count(9)):
            return True
    else:
        subarray=nums[0:3]
        if (subarray.count(9)):
            return True
            
    return False
   
  

print array_front9([1,9,3,4,9])
