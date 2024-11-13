"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
"""

"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        if not head.next.next:
            return ListNode(val = head.next.val, next = ListNode(val = head.val))
        
        linked_list = []
        while head:
            linked_list.append(head.val)
            head = head.next
        head = ListNode(val=linked_list[-1])
        dummy = ListNode(next=head)
        for value in linked_list[-2::-1]:
            print(value)
            head.next = ListNode(val = value)
            head = head.next
        return dummy.next
