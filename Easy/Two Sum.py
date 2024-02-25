def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
def twoSum2(nums,target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        numMap[nums[i]] = i

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[nums[i]] != i:
            return [i,numMap[complement]]
    return []
def twoSum3(nums,target):
    numMap = {}
    n = len(nums)

    for i in range(n):
        complement = target - nums[i]
        if complement in numMap:
            return [numMap[complement], i]
        numMap[nums[i]] = i


print(twoSum([2,5,5,11],10))
print(twoSum2([2,5,5,11],10))
print(twoSum3([2,5,5,11],10))