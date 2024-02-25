def dailyTemperatures(temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    result = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures)-1,-1,-1):
        cur_temp = temperatures[i]
        while stack and cur_temp >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)
    return result
print(dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))