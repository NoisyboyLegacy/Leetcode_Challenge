def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    l, r = 0, 0
    res = {}
    n = len(s)
    lenn = 0
    while r < n:
        if s[r] in res:
            l = max(res[s[r]] + 1, l)
            res[s[r]] = r
        else:
            res[s[r]] = r
        lenn = max(lenn, (r - l) + 1)
        r += 1
    return lenn


print(lengthOfLongestSubstring(s="pwwkew"))
