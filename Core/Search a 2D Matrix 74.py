def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        print(matrix[i][0], matrix[i][-1])
        if target > matrix[i][0] and i != 0 and i == len(matrix):
            target_layer = matrix[i - 1]
            # print("larger")
            break
        elif target <= matrix[i][-1]:
            target_layer = matrix[i]
            # print("smaller")
            break
    else:
        # print("false")
        return False
    # print(target_layer)
    for i in target_layer:
        if i == target:
            return True
    return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(searchMatrix([[1],[3]], 3))
print(searchMatrix([[1],[3],[5]], 5))