# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def rec(node, p, q): 
            if not node: return None 

            if node.val == p or node.val == q: 
                return node 
            
            left = rec(node.left, p, q)
            right = rec(node.left, p, q)

            if left and right: 
                return node 
            else: 
                return left or right
        
        return rec(root, p, q)
