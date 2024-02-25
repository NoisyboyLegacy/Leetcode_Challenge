import heapq


def kClosest(points, k):
    """
    :type points: List[List[int]]
    :type k: int
    :rtype: List[List[int]]
    """
    heap = []
    for x, y in points:
        dist = -(x * x + y * y)
        if len(heap) == k:
            heapq.heappushpop(heap, (dist, x, y))
        else:
            heapq.heappush(heap, (dist, x, y))
    return [(x, y) for dist, x, y in heap]


print(kClosest(points=[[3, 3], [5, -1], [-2, 4]], k=2))
