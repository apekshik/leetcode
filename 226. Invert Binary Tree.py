# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def rec(node):
            if not node: 
                return 
            # swap nodes. 
            node.left, node.right = node.right, node.left
            # recursively go down the left and right subtrees and do the same. 
            rec(node.left)
            rec(node.right)
            
        rec(root)
        return root


        

