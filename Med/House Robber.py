def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    odd, eve = 0,0
    for i in nums:
        temp = max(odd+i,eve)
        odd = eve
        eve = temp
    return eve
print(rob(nums = [1,2,3,1]))