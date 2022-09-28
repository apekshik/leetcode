class Node:
    def __init__(self, left=None, right=None, val=None):
        self.left = left 
        self.right = right 
        self.val = val 


class Solution: 
    def inOrder(self, root: Node): 
        def rec(node):
            if not node: 
                return
            # we recurse into the left node. 
            rec(node.left)
            # process the current node 
            print(node.val)
            # recurse into the right node. 
            rec(node.right)
        
        def iter(root): 
            stack = [] 
            cur = root
            while cur or stack: 
                # keep going down the left sub tree until you hit null. 
                while cur: 
                    stack.append(cur)
                    cur = cur.left 
                
                # process the cur node 
                cur = stack.pop()
                print(cur.val)
                # switch to the right node which will get added to the stack in the next 
                # iteration of the while loop. 
                cur = cur.right 
                

