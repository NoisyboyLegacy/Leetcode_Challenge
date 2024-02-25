def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    map = {}
    ans = []
    for str in strs:
        sorted_str = "".join(sorted(str))
        if sorted_str in map:
            ans[map[sorted_str]].append(str)
        else:
            map[sorted_str] = len(ans)
            ans.append([str])
    return ans
print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))