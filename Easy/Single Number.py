def singleNumber(nums):
    uniqNum = 0
    for idx in nums:
        uniqNum ^= idx
    return uniqNum
print(singleNumber(nums = [4,1,2,1,2]))