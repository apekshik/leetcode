# 515. Find Largest Value in Each Tree Row

from collections import Optional, List
import deque
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        q.appendleft(root) # could just be append but used appendleft for consistency's sake.  
        
        res = [] 
        temp = [] 
        while q: 
            qLen = len(q) # so you know the width of the current layer of the queue.
            for i in range(qLen): 
                node = q.pop() 
                if node: # in case node is NoneObj
                    temp.append(node.val)
                    q.appendleft(node.left)
                    q.appendleft(node.right)

            if temp: # in case temp is empty. 
                mx = max(temp)
                res.append(mx)
            temp = [] 
            
        
        return res

