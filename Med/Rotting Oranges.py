from collections import deque


def orangesRotting(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    cols = len(grid[0])
    if rows == 0:
        return -1
    fresh_org = 0
    rotten = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                rotten.append((r, c))
            elif grid[r][c] == 1:
                fresh_org += 1
    minutes = 0
    while rotten and fresh_org > 0:
        minutes += 1
        for _ in range(len(rotten)):
            x, y = rotten.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                xx, yy = x + dx, y + dy
                if xx < 0 or xx >= rows or yy < 0 or yy >= cols:
                    continue
                if grid[xx][yy] == 0 or grid[xx][yy] == 2:
                    continue
                fresh_org -= 1
                grid[xx][yy] = 2
                rotten.append((xx, yy))
    return minutes if fresh_org == 0 else -1


print(orangesRotting(grid=[[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
