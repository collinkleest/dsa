# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from list_node import ListNode


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative approach
        # TC: O(N) (linear), SC: O(1)
        
        prev, curr = None, head
        
        while curr.next != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
        # recursive approach
        # TC: O(N) (linear), SC: O(N)
        if not head:
            return None
        
        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return newHead
       
            
        