# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional 

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # in the case you're given a null head. 
        if head is None or head.next is None: 
            return head

        # in all other cases, proceed as follows: 
        # 1 -> 2 -> 3 -> 4 -> None 
        # ^    ^    ^ 
        # prev curr temp
        # current.next should point to previous. Previous is moved to current. Current is moved to temp
        # since reassigning current to previous lost the information for node 3. 
        prev = head
        curr = head.next 
        temp = None 

        while curr: 
            temp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = temp 

        return prev 

# Create a linked list with nodes
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)

# Link the nodes together
n1.next = n2
n2.next = n3
n3.next = n4

# Function to print the values of the linked list for testing
def print_list(node):
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values

# Test the reverseList function
S = Solution()
reversed_list_head = S.reverseList(n1)
print_list(reversed_list_head)