def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    dp, s = {0}, sum(nums)
    if s & 1:
        return False
    for num in nums:
        for curr in range(s >> 1, num - 1, -1):
            if curr not in dp and curr - num in dp:
                if curr == s >> 1:
                    return True
                dp.add(curr)
    return False


print(canPartition(nums=[1, 5, 11, 5]))
