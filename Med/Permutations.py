def permute(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def solve(nums, per, c):
        if c == len(nums):
            ans.append(list(per))
        for i in range(len(nums)):
            if per[i] == 11:
                per[i] = nums[i]
                solve(nums, per, c + 1)
                per[i] = 11
        return ans

    ans = []
    per = [11] * len(nums)
    solve(nums, per, 0)
    return ans


print(permute(nums=[1, 2, 3]))
