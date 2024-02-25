def letterCombinations(digits):
    """
    :type digits: str
    :rtype: List[str]
    """
    phone = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []

    def backtrack(comb,next_digit):
        if not next_digit:
            res.append(comb)
            return
        for letter in phone[next_digit[0]]:
            backtrack(comb + letter,next_digit[1:])

    backtrack("",digits)
    return res
print(letterCombinations(digits = "23"))