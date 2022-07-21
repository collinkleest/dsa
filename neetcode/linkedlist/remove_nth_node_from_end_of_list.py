# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from neetcode.linkedlist.list_node import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pass algo
        # get the length of the list
        # if the length is less than or equal to 1 return None
        
        # get length of linked list
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        # if our length is one we just want to return None or the next element which will be None
        if length == n:
            return head.next
        
        curr = head
        
        indexOfNodeBefore = length - n - 1
        
        for i in range(indexOfNodeBefore):
            curr = curr.next
        
        curr.next = curr.next.next
        return head   

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single pass solution
        # O(N)
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
        
        while right:
            right = right.next
            left = left.next
            
        left.next = left.next.next
        return dummy.next
        