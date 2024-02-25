from collections import Counter


def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    counts = list(Counter(tasks).values())
    most_repeats = max(counts)
    num_longest = counts.count(most_repeats)
    return max(len(tasks), (most_repeats - 1) * (n + 1) + num_longest)
print(leastInterval(tasks = ["A","A","A","A","A","A","B","B","B","B"], n = 2))