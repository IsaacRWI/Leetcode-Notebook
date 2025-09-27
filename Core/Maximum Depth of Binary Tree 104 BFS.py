from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def maxDepth(self, root) -> int:
    if not root:  # if tree is empty
        return 0
    level = 0
    q = deque([root])  # double-ended queue
    while q:  # whilst queue is not empty
        for i in range(len(q)):  # for item in queue at this time  # doing it this way will not loop through the newly added nodes  i think
            node = q.popleft()  # removed leftmost item in list
            if node.left:  # if node has a left child
                q.append(node.left)  # append left child to queue
            if node.right:  # same for right
                q.append(node.right)
        level += 1  # add 1 to counter at the end of the for loop  so the while loop can run again with the newly appended nodes
    return level  # return level when queue is empty