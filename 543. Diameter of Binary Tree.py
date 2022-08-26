# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0] # stores the max diameter size. 

        def rec(root):
            if not root: 
                return -1
            
            left = rec(root.left) # returns max depth from left child.
            right = rec(root.right) # returns max depth from right child. 
            # recursively find the max at each node and compare it with global result. 
            res[0] = max(res[0], 2 + left + right) 

            # this step is necessary for the left and right values above to have 
            # the correct values. 
            return 1 + max(left, right) 

        #call the recursive function. 
        rec(root)
        return res[0]


            