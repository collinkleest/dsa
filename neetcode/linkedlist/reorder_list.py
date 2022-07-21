# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from neetcode.linkedlist.list_node import ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # TC: O(N), SC: O(1)
        # find middle of list
        # use slow and fast pointers, slow will alows get to the middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        

        # now reverse the second part of the list
        second = slow.next
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge the two halfs
        # our second should now point to previous
        # since our second is pointing to None now
        # and our first half will just point to the current head
        second, first = prev, head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        