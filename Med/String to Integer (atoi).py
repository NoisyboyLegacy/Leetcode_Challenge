def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    n, MIN, MAX, empty, sign = 0, -2 ** 31, 2 ** 31 + 1, True, 1
    for char in s:
        if empty:
            if char == " ":
                continue
            elif char == "-":
                sign = -1
            elif char.isdigit():
                n = int(char)
            elif char != "+":
                return 0
            empty = False
        else:
            if char.isdigit():
                n = n*10 + int(char)
                if sign*n > MAX:
                    return MAX
                elif sign*n < MIN:
                    return MIN
            else:
                break
    return n*sign





print(myAtoi(s="-4193 with words"))
