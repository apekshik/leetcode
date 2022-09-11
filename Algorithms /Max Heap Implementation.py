class TreeNode: 
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right 
    

class MaxHeap:
    def __init__(self, root: TreeNode = None, last: TreeNode = None):
        self.root = root 
        self.lastLeaf = last

    def insert(self, element: int) -> None: 
        if not self.root: 
            self.root = TreeNode(element) 

    def extractMax(self) -> int:
        res = self.root.val 
        

