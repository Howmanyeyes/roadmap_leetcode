"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description/
"""

"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Мы можем итерировать по самому длиному списку и держать в себе нумерацию ноды. Каждое новое
полученое число из ноды мы умножаем на 10^[итерация] сес? Мы ничего не храним, когда одна из нод
кончится мы просто будем игнорировать ее, можно сделать 3 кейса ифами, позже оптимизировать
"""

# Definition for singly-linked list.

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        iterr = 0
        summ = 0
        #num1 = l1.val
        #num2 = l2.val
        while l1.next or l2.next:
            
            # summ += (num1 + num2) * 10**iter
            if l1:
                summ += l1.val * 10**iterr
                l1 = l1.next
            if l2:
                summ += l2.val * 10**iterr
                l2 = l2.next
            iterr += 1
        root = ListNode(0)
        head = root # 7 0 8 | 0 | 0->7 | check 
        for digit in str(summ)[::-1]:
            head.next = ListNode(int(digit))
            head = head.next
        return root.next