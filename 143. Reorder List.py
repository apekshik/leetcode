# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # helper function to reverse linked list. 
    
        slow = head
        fast = slow.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next # double the speed of the slow pointer. 
        
        first = head 
        second = slow.next 
        
        # reverse the second list first.
        prev = slow.next = None 
        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp
            
        second = prev 
        
        # merge the two linked lists in an alternating pattern. 
        while second: 
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            
        
        