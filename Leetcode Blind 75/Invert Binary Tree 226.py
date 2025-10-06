class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def invertTree(root):
    if not root:  # if tree is empty
        return None

    tmp = root.left  # temporary variable to store left value for root
    root.left = root.right  # switch left tree value with right
    root.right = tmp  # switch right tree value with left

    invertTree(root.left)  # call function on left tree   # recursively calling on the function itself
    invertTree(root.right)  # call function on right tree
    return root
