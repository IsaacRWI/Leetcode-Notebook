def searchMatrix(matrix, target):
    for i in range(len(matrix)):  # for item index in matrix
        # print(matrix[i][0], matrix[i][-1])  # prints first number in the item and last number in the item

        # this statement is not needed
        """
        if target > matrix[i][0] and i != 0 and i == len(matrix):
        # if target is larger than first number in item, and it's not the first item, and it's the last item in the matrix
            target_layer = matrix[i - 1]  # sets the target_layer to the item before this one
            # print("larger")
            break
        """

        if target <= matrix[i][-1]:  # if target is smaller or equal to last number in the item
            target_layer = matrix[i]  # sets target_layer to current item
            # print("smaller")
            break
    else:
        # print("false")
        return False  # if target is not smaller than any last numbers in the items, reutrn false
    # print(target_layer)
    for i in target_layer:
        if i == target:
            return True
    return False

# print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
# print(searchMatrix([[1],[3]], 3))
print(searchMatrix([[1],[3],[5]], 5))