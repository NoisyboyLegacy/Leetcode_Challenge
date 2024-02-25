def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    max_prod = float('-inf')
    cur_prod = -1
    for i in range(n):
        cur_prod *= nums[i]
        max_prod = max(max_prod,cur_prod)
        if cur_prod == 0:
            cur_prod = 1
    cur_prod =1
    for i in range(n-1,-1,-1):
        cur_prod *= nums[i]
        max_prod = max(max_prod,cur_prod)
        if cur_prod == 0:
            cur_prod = 1
    return max_prod
print(maxProduct(nums = [2,3,-2,4]))