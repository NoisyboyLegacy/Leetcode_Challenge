def missingNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    for counter, value in enumerate(nums):
        result ^= counter+1
        result ^= value
    return result
print(missingNumber([9,6,4,2,3,5,7,0,1]))