def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    squares = [[set() for _ in range(3)] for _ in range(3)]

    for x in range(9):
        for y in range(9):
            cell_value = board[x][y]
            if cell_value == ".":
                continue
            if cell_value in rows or cell_value in cols or cell_value in squares[x//3][y//3]:
                return False
            rows[x].add(cell_value)
            cols[y].add(cell_value)
            squares[x//3][y//3].add(cell_value)
    return True
print(isValidSudoku(board =
                [["5","3",".",".","7",".",".",".","."]
                ,["6",".",".","1","9","5",".",".","."]
                ,[".","9","8",".",".",".",".","6","."]
                ,["8",".",".",".","6",".",".",".","3"]
                ,["4",".",".","8",".","3",".",".","1"]
                ,["7",".",".",".","2",".",".",".","6"]
                ,[".","6",".",".",".",".","2","8","."]
                ,[".",".",".","4","1","9",".",".","5"]
                ,[".",".",".",".","8",".",".","7","9"]]))