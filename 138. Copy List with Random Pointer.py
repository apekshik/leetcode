
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # handle edge cases
        if not head: 
            return None 
        
        # create a hashmap OldToNew that maps old nodes to new ones 
        # as well as creating the new list with the next pointers and vals. 
        # don't need to set the random nodes right now. We do it later. 
        
        otn = {} # "old to new" hashmap.  
        
        # iterate through old list and populate otn. 
        h = head 
        while h: 
            n = Node(h.val) # next and random are null now but we'll assign them next.  
            otn[h] = n 
            h = h.next
        
        # look back at the head of the old list and iterate through it again. 
        h = head 
        # for each node, see which random node it's pointing to and then use the
        # hashmap to create the same connections in our new list. 
        while h: 
            # connect the next edge first
            if h.next: 
                otn[h].next = otn[h.next]
            # connect the random edge then. 
            if h.random: 
                otn[h].random = otn[h.random]
            h = h.next
            
        return otn[head] 
        