class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def maxDepth(self, root) -> int:
    if not root:  # if tree is empty
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))  # recursively calls the function to get number of children on left and right roots then adds 1 for current depth