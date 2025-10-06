def searchMatrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])
    top = 0
    bot = rows - 1
    while top <= bot:
        mid = (top + bot) // 2
        if target > matrix[mid][-1]:
            top = mid + 1
        elif target < matrix[mid][0]:
            bot = mid - 1
        else:
            break
    if not (top <= bot):
        return False

    row = (top + bot) // 2
    l = 0
    r = columns - 1
    while l <= r:
        mid = (l + r) // 2
        if target > matrix[row][mid]:
            l = mid + 1
        elif target < matrix[row][mid]:
            r = mid - 1
        else:
            return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
print(searchMatrix([[1],[3]], 3))
print(searchMatrix([[1],[3]], 4))