class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        if not subRoot:  # if subRoot is empty then we assume the main tree contains it as its empty
            return True
        if not root and subRoot:  # if main tree is empty and subtree isnt
            return False
        if self.sameTree(root, subRoot):  # see if the subtree is the same as main tree
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))  # recursively seeing if the left and right branches are the same as the subtree

    def sameTree(self, s, t):  # same tree function to use in main function
        if not s and not t:  # if both trees are empty
            return True
        if s and t and s.val == t.val:  # if both trees exist and their values are the same
            return (self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right))  # return if the left and right branches elements are the same recursively
        return False  # else return false
