import collections

def isValidSudoku(board) -> bool:
    rows = collections.defaultdict(set)  # sets to for the algorithm to check if the number has already appeared in the row
    cols = collections.defaultdict(set)  # column
    square = collections.defaultdict(set)  # or square

    for r in range(len(board[0])):  # for row(list in the list of lists that make up the board)
        for c in range(len(board[0])):  # for numbers in the list
            if board[r][c] == ".":  # if the value in the list is empty
                continue  # skip the loop on this one and don't add it to the set

    # basically the c index is the pointer going through all the values in the board
    # if c is already in any of the lists ie the row(list) its in or column(list by index) or the square return False
    # else add c to all 3 of these lists

            if (board[r][c] in rows[r] or  # if the number the pointer is on rn is in the sets rows
                board[r][c] in cols[c] or  # columns
                board[r][c] in square[(r // 3, c // 3)]):  # or squares

                # the square set works by taking the indexes for rows and columns and divides them and rounds down by 3
                # 0, 1, 2 //3 will be 0,  3, 4, 5 //3 will be 1, and 6, 7, 8 //3 will be 2
                # it then takes the row and column square the pointer is in as the key for the dict and adds c index value into the set if it's not already there

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

