def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l = 0
    r = len(height) - 1
    while l<r:
        area = (r-l) * min(height[r],height[l])
        maxarea = max(maxarea,area)
        l+=1
    return maxarea


print(maxArea(height = [1,8,6,2,5,4,8,3,7]))