from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def maxDepth(self, root) -> int:
    if not root:
        return 0

    stack = [[root, 1]]  # stack contains the nodes in the tree and their depths
    res = 1  # result = at least 1 as there is a root node
    while stack:  # whilst stack is not empty
        node, depth = stack.pop()  # remove node from stack

        if node:  # if node is not null
            res = max(res, depth)  # result = max depth so far
            stack.append([node.left, depth + 1])  # append the children of the node to the stack and their depth
            stack.append([node.right, depth + 1])

    return res