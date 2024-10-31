"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/description/?envType=problem-list-v2&envId=hash-table
"""

"""
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect.
If the two linked lists have no intersection at all, return null.

Didn't have enough time to finish this one. Interesting problem, f***s my brain, done simple
approach using O(m*n) time which was not suffisient. Now solution is based on determining shortest 
head and scanning only it twice. So worst case scenario it is still O(2min(m, n)), but i hope this
solution will be sufficient. Right now tests are not passed because point of intersection is not
determined correctly. My program returns next value to correct one.

"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        original_B = headB
        original_A = headA
        hash_map_A = {}
        hash_map_B = {}
        hash_map_A[headA] = headA
        hash_map_B[headB] = headB
        i = 1
        len_A = 1
        len_B = 1
        stop_A, stop_B = False, False
        while not (stop_A and stop_B):
            if headA.next is None:
                stop_A = True
            else:
                headA = headA.next
                hash_map_A[headA] = headA
                len_A += 1
            if headB.next is None:
                stop_B = True
            else:
                headB = headB.next
                hash_map_B[headB] = headB
                len_B += 1
        short_head = "A"
        long_head = "B"
        if len_A > len_B:
            short_head = "B"
            long_head = "A"
        least_len = {
            "A": original_A,
            "B": original_B
        }
        least_map = {
            "A": hash_map_A,
            "B": hash_map_B
        }
        shortest = least_len.get(short_head)
        longest_hash = least_map.get(long_head)
        if longest_hash.get(shortest, False):
            return shortest
        while shortest.next is not None:
            if longest_hash.get(shortest, False):
                return shortest
            shortest = shortest.next
        if longest_hash.get(shortest, False):
            return shortest 
        return None



if __name__ == '__main__':
    shared = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, shared))
    headB = ListNode(5, ListNode(6, ListNode(1, shared)))
    
    print(Solution().getIntersectionNode(headA, headB))