# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

pathBuilder = [] 
pathMap = {}
def step(node, s): 
    if node.val == s: 
        print("Found value: ", node.val)
        return node 
    
    left = right = None 
    if node.left:
        left = step(node.left, s) 
    if node.right: 
        right = step(node.right, s)
    
    if left or right:
        pathBuilder.append("L" if left else "R")
        return left or right 

Root = Node(0)
Root.left = l1 = Node(1)
Root.right = r1 = Node(2) 
l1.left = l2 = Node(3) 
l1.right = r2 = Node(4) 
r1.left = l3 = Node(5) 
r1.right = r3 = Node(6) 
l2.left = l4 = Node(7) 
l2.right = r4 = Node(8) 
r2.left = l5 = Node(9) 
r2.right = r5 = Node(10) 
l3.left = l6 = Node(11)
l3.right = r6 = Node(12)
r3.left = l7 = Node(13)
r3.right = r7 = Node(14)

step(Root, 12)
print(pathBuilder)