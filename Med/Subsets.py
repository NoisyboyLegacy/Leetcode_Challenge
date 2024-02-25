def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    arr = [[]]
    for j in nums:
        arr+=[i + [j] for i in arr]
    return arr
print(subsets(nums = [1,2,3]))