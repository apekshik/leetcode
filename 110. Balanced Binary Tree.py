import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# A binary tree in which the left and right subtrees of every node differ 
# in height by no more than 1.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        temp = [True]
        if not root: 
            return temp[0]
        
        def rec(node: TreeNode) -> int: 
            if not node: # a leaf node
                return 0
            
            leftHeight = rec(node.left)
            rightHeight = rec(node.right)
            
            if abs(leftHeight - rightHeight) > 1: 
                temp[0] = False 
            
            return 1 + max(leftHeight, rightHeight)
         
        rec(root)
        return temp[0]