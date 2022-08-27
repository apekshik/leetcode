import collections 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()
                if node: # to make sure null nodes aren't accessed via the dot operator. 
                    level.append(node.val)
                    q.append(node.left) # possible appending of null nodes here
                    q.append(node.right) # and here which we deal with using an if statement above.
            if level: # to make sure empty lists aren't appended to result array.
                res.append(level)

        return res
