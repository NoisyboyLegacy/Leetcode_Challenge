def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = [c.lower() for c in s if c.isalnum()]
    return all(s[i] == s[~i] for i in range(len(s) // 2))

print(isPalindrome(s = "A man, a plan, a canal: Panama"))