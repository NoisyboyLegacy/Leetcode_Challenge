def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    freq_s = {}
    for ch in s:
        freq_s[ch] = freq_s.get(ch, 0) + 1
    odd = False
    ans = 0
    for value in freq_s.values():
        if value % 2 == 0:
            ans += value
        else:
            ans = ans + value - 1
            odd = True
    if odd:
        ans += 1
    return ans
print(longestPalindrome(s = "abccccdd"))