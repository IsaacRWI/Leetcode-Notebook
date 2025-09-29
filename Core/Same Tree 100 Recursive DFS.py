class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def isSameTree(self, p, q) -> bool:
    if not p and not q:  # if both p and q nodes are null then they are the same
        return True
    if not p or not q or p.val != q.val:  # if one of the nodes is null or if the values arent equal
        return False
    return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))  # recursively call function for leaves of the tree