"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers_v1(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1 + v2 + carry, 10)
            n.next = n = ListNode(val)
        return root.next


    def addTwoNumbers_v2(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        head = l1
        carryOn = (l1.val + l2.val) / 10
        l1.val = (l1.val + l2.val) % 10
        while l1.next != None and l2.next != None:
            carryOn += l1.next.val
            carryOn += l2.next.val
            l1.next.val = carryOn % 10
            carryOn = carryOn // 10
            l1 = l1.next
            l2 = l2.next
        if l1.next == None:
            l1.next = l2.next
        while l1.next != None:
            carryOn += l1.next.val
            l1.next.val = carryOn % 10
            carryOn = carryOn // 10
            l1 = l1.next
        if carryOn > 0:
            l1.next = ListNode(carryOn)
        return head


    def addTwoNumbers_v3(self, l1, l2):
        head = ListNode(0)
        l = head
        carry = 0
        while l1 or l2 or carry:
            sum, carry = carry, 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            if sum > 9:
                carry = 1
                sum -= 10
            l.next = ListNode(sum)
            l = l.next
        return head.next