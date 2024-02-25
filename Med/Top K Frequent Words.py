from collections import Counter


def topKFrequent(words, k):
    """
    :type words: List[str]
    :type k: int
    :rtype: List[str]
    """
    map = {}
    ans = []
    for word in words:
        map[word] = map.get(word,0)+1
    map = sorted(map.items(),key= lambda k:(-k[1],k[0]))
    for tup in map:
        ans.append(tup[0])
        k-=1
        if k ==0 :
            break
    return ans
print(topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))