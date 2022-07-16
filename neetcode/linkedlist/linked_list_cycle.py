# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import Optional

from neetcode.linkedlist.list_node import ListNode


class Solution:
    # Using hashset solution
    # O(N) time complexity, and O(N) space complexity
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        
        while head:
            if head in hash_set:
                return True
            hash_set.add(head)
            head = head.next
        
        return False
    

    # Floyds Tortoise and Hare Algorithm
    # Fast pointer and slow pointer are going to meet eventually
    # O(N) time complexity, O(1) space complexity
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False