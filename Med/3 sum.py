def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = set()
    n, p, z = [], [], []
    for num in nums:
        if num > 0:
            p.append(num)
        if num < 0:
            n.append(num)
        if num == 0:
            z.append(num)

    N, P = set(n), set(p)
    if z:
        for num in P:
            if -num in N:
                res.add((-num, 0, num))
    if len(z) >= 3:
        res.add((0, 0, 0))
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            target = -(n[i] + n[j])
            if target in P:
                res.add(tuple(sorted([n[i], n[j], target])))
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            target = -(p[i] + p[j])
            if target in P:
                res.add(tuple(sorted([p[i], p[j], target])))
    return res


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
