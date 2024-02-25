from collections import Counter


def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    sliding, ranger = len(p), len(s)
    count_p, count_slide = Counter(p), Counter(s[:sliding-1])
    ans = []
    j = 0
    for i in range(sliding-1,ranger):
        count_slide[s[i]] +=1
        if count_p == count_slide:
            ans.append(j)
        count_slide[s[j]] -=1
        if count_slide[s[j]] == 0:
            del count_slide[s[j]]
        j+=1
    return ans
print(findAnagrams(s = "cbaebabacd", p = "abc"))