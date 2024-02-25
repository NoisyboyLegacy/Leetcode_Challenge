def moveZeroes(nums):
    index = 0
    # Place non-zero elements at the start of the list
    for num in nums:
        if num != 0:
            nums[index] = num
            index += 1
    # Fill the remaining positions with zeroes
    while index < len(nums):
        nums[index] = 0
        index += 1
    return nums

print(moveZeroes([0,1,0,3,12]))