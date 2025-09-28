class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isBalanced(self, root) -> bool:
    def dfs(root):  # recursive function for depth first search
        if not root:  # if root is null
            return [True, 0]  # return true because even if its empty its balanced

        left = dfs(root.left)  # recursive function for left leaves
        right = dfs(root.right)

        balance = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)  # checking if the sub trees are balanced
        # the height is for checking if the trees are balanced, if they have the same height +- 1 then theyre balanced
        return [balance, 1 + max(left[1], right[1])]  # return if its balanced and the height of the tree so far cleared

    return dfs(root)[0]  # call recursive function on tree