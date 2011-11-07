def big_diffs(nums):
    nums.sort()
    return nums[len(nums)-1]-nums[0]

print big_diffs([2,10,7,2])
