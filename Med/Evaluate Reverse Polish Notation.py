def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    for token in tokens:
        if len(token) == 1 and ord(token) < 48:
            num2 = stack.pop()
            num1 = stack.pop()
            result = resolve(num1, num2, token)
            stack.append(result)
        else:
            stack.append(int(token))
    return stack.pop()


def resolve(a, b, ope):
    if ope == '+':
        return a + b
    elif ope == '-':
        return a - b
    elif ope == '*':
        return a * b
    return int(a / b)


print(evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
