# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev 
            prev = cur
            cur = temp
            
        return prev
            

#recursive solution to the reverse linked list problem. 
class Solution2: 
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        #Global variable to store newHead pointer to return finally. 
        newHead = [ListNode()]

        def rec(head: ListNode):
            if head.next:
                # print(head.val)
                tail = rec(head.next)
                tail.next = head 
                head.next = None 
                # print(tail.val, head.val)
            else: 
                # print("head value at end of list:", head.val)
                newHead[0] = head
            # print(head.val)
            return head 

        rec(head)
        return newHead[0]
        
    
    

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4 

S = Solution2()
res = S.reverseList(node1)
while res:
    print(res.val)
    res = res.next