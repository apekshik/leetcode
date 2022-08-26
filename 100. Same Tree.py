# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if both nodes don't exist, you can return true.
        if not p and not q: 
            return True 
        
        # if one of the nodes don't exist, trees p and q aren't the same so must return false.
        if not p or not q: 
            return False 
    
        # final check that the values p and q nodes contain match or not. 
        if p.val != q.val: 
            return False 
        
        right = self.isSameTree(p.right, q.right)
        left = self.isSameTree(p.left, q.left)
        return left and right