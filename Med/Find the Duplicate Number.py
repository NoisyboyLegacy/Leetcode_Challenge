from collections import Counter


def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    dict = Counter(nums)
    for i in dict:
        if dict[i]>= 2:
            return i

print(findDuplicate(nums = [1,3,4,2,2]))