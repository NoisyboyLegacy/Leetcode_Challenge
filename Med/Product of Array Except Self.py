def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    product = [1] * length
    for i in range(1, length):
        product[i] = nums[i - 1] * product[i - 1]
    right = nums[-1]
    for i in range(length - 2, -1, -1):
        product[i] *= right
        right *= nums[i]
    return product


print(productExceptSelf(nums=[1, 2, 3, 4]))
