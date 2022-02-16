# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #
        #   Linked List   
        #   two adjacent nodes
        #   RETURN head
        #   CONSTRAINT: without modifying the values 
        #             [0, 100]
        #   Reverse linked list ??? 
        curr = head
        if curr is None:
            return None
        if curr.next is None:
            return curr
        new_head = curr.next
        prev = None
        while curr is not None and curr.next is not None:
            nxt = curr.next.next
            left = curr
            right = curr.next
            right.next = left
            left.next = nxt
            if prev is not None:
                prev.next = right
            prev = left
            curr = nxt
        return new_head
        
        
        
