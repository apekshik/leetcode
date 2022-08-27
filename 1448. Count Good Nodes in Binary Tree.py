# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        res = [0]

        def dfs(root: TreeNode, m: int) -> None:
            # base case
            if not root: 
                return 
            # if bad node detected continue recursion. 
            if root.val < m: 
                dfs(root.left, m)
                dfs(root.right, m)
            else:
                res[0] += 1
                m = max(m, root.val)
                dfs(root.left, m)
                dfs(root.right, m)
        
        dfs(root, root.val)
        return res[0]