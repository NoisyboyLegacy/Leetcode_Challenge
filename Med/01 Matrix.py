from collections import deque


def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    m, n = len(mat), len(mat[0])
    queue = deque()
    result = [row[:] for row in mat]
    visited = set()

    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0:
                result[i][j] = 0
                visited.add((i, j))
                queue.append((i, j, 0))

    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    while queue:
        row, col, steps = queue.popleft()
        for dr, dc in directions:
            next_row, next_col, next_steps = row + dr, col + dc, steps + 1
            if 0 <= next_row < m and 0 <= next_col < n and (next_row, next_col) not in visited:
                result[next_row][next_col] = next_steps
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, next_steps))
    return result


print(updateMatrix(mat=[[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
