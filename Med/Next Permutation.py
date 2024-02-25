def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 2
    j = len(nums) - 1
    while i >= 0 and nums[i] >= nums[i+1]:
        i-=1
        if i == -1:
            nums.reverse()
            return nums
    while nums[j] <= nums[i]:
        j-=1
    nums[j],nums[i] = nums[i],nums[j]
    nums[i+1:] = reversed(nums[i+1:])
    return nums
print(nextPermutation(nums = [1, 3, 2]))
