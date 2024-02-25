def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: bool
    """
    tracker = [True] + [False] * len(s)
    for right in range(len(s) + 1):
        for left in range(len(s)):
            if tracker[left] and s[left:right] in wordDict:
                tracker[right] = True
    return tracker[-1]


print(wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"]))
