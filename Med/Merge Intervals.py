def merge(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[List[int]]
    """
    intervals.sort(key=lambda x: x[0])
    merge = [intervals[0]]
    for interval in intervals:
        if merge[-1][1] < interval[0]:
            merge.append(interval)
        else:
            merge[-1][1] = max(merge[-1][1], interval[1])
    return merge


print(merge(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
