# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def valid(node: TreeNode, left: int, right: int) -> bool:
            if not node: # we've reached an null node so return true
                return True

            if node.val > right and node.val < left: 
                return False 
            
            return valid(node.left, left, node.val) and valid(node.right, node.val, right)
        
        return valid(root, float("-inf"), float("inf"))
