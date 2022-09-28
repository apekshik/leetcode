# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # extract all nodes into an array, sort it and return the kth smallest element. 
        
        # to extract we use InOrder traversal, since it gives us values in sorted order 
        # for a binary search tree. 
        
        stack = [] 
        cur = root 
        while cur and stack:
            while cur: 
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val  
            cur = cur.right 

        # recursive solution. Just call this with root as argument. 
        def rec(node):
            if not node: 
                return  
            rec(node.left)
            k -= 1
            if k == 0: 
                return node.val 
            rec(node.right) 
            k -= 1