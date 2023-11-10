# Arrays
array = [1, 2, 3, 4, 5]

# Sets
set_data = {1, 2, 3, 4, 5}

# Matrices
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Heaps
import heapq
heap = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapq.heapify(heap)  # Transforms list into a heap, in-place, in linear time

# Adding an element to the heap
heapq.heappush(heap, 10)
# Removing and returning the smallest element
smallest = heapq.heappop(heap)
# Getting the smallest element without popping
smallest = heapq.nsmallest(1, heap)[0]

# Binary Trees
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    # Methods to insert, search would be defined here

# Linked Lists
class ListNode: 
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None 

# Dictionary (hash map)
dictionary = {'key1': 'value1', 'key2': 'value2'}

# Queues
from collections import deque
queue = deque(['a', 'b', 'c'])

# Stacks
stack = [1, 2, 3]
stack.append(4)  # Push
stack.pop()      # Pop

# Copy Method
import copy
copied_list = copy.deepcopy(array)  # Deep copy of a list


'''A shallow copy creates a new object that is a copy of the original object, but it doesn't recursively copy the objects contained within. 
So, if the original object contains other objects (e.g., nested lists or objects), those nested objects will still refer to the same objects 
in memory in both the original and the shallow copy.'''
# Shallow Copy Method: 
original_list = [1, 2, 3, 4, 5]

# Create a shallow copy of the list
shallow_copy = copy.copy(original_list)

# Modify the shallow copy
shallow_copy[0] = 10

# The original list remains unchanged
print(original_list)  # Output: [1, 2, 3, 4, 5]
print(shallow_copy)   # Output: [10, 2, 3, 4, 5]