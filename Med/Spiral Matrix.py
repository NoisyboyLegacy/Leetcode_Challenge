def spiralOrder(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    result = []
    while matrix:
        result += matrix.pop(0)
        matrix = list(zip(*matrix))[::-1]
    return result
print(spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]]))