def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    tail = [0] * len(nums)
    size = 0
    for num in nums:
        i,j = 0,size
        while i !=j:
            m = (i+j) //2
            if tail[m] < num:
                i = m+1
            else:
                j = m
        tail[i] = num
        size = max(size,i+1)
    return size
print(lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))