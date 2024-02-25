def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    arr = []
    arr.append(nums[0])
    maxSum = arr[0]
    for i in range(1, len(nums)):
        arr.append(max(arr[i - 1] + nums[i], nums[i]))
        if arr[i] > maxSum:
            maxSum = arr[i]
    return maxSum
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))