def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    count_map = {}

    for num in nums:
        count_map[num] = count_map.get(num, 0) + 1
        if count_map[num] > n / 2:
            return num

    return -1

print(majorityElement(nums = [2,2,1,1,1,2,2]))
