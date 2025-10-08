import collections

def isValidSudoku(board) -> bool:
    rows = collections.defaultdict(set)  # sets to for the algorithm to check if the number has already appeared in the row
    cols = collections.defaultdict(set)  # column
    square = collections.defaultdict(set)  # or square

    for r in range(len(board[0])):  # for row(list in the list of lists that make up the board)
        for c in range(len(board[0])):  # for numbers in the list
            if board[r][c] == ".":  # if the value in the list is empty
                continue  # skip the loop on this one and don't add it to the set
            if (board[r][c] in rows[r] or  # if the number the pointer is on rn is in the sets rows
                board[r][c] in cols[c] or  # columns
                board[r][c] in square[(r // 3, c // 3)]):  # or squares
                return False
            # else
            cols[c].add(board[r][c])  # add the number to the set for column
            rows[r].add(board[r][c])  # for the rolls
            square[(r // 3, c // 3)].add(board[r][c])  # and for the square
    return True  # if reached end of list without returning False, return True

print(isValidSudoku([["5","3",".",".","7",".",".",".","."],
                     ["6",".",".","1","9","5",".",".","."],
                     [".","9","8",".",".",".",".","6","."],
                     ["8",".",".",".","6",".",".",".","3"],
                     ["4",".",".","8",".","3",".",".","1"],
                     ["7",".",".",".","2",".",".",".","6"],
                     [".","6",".",".",".",".","2","8","."],
                     [".",".",".","4","1","9",".",".","5"],
                     [".",".",".",".","8",".",".","7","9"]]))

