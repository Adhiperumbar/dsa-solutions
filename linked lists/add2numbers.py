"""
Date: 07-09-2025
Problem: Add Two Numbers (LeetCode 2)
Problem Statement:
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each node contains a single digit. Add the two numbers and return the sum as a linked list.
Approach:
Use a dummy head node to simplify linked list construction.
Maintain a carry while adding digits.
Traverse both lists (l1, l2) simultaneously:
Extract digits val1 and val2 (use 0 if a list is exhausted).
Compute tot = val1 + val2 + carry.
Update carry = tot // 10 and digit dig = tot % 10
Create a new node with dig and link it.
Continue until both lists and carry are exhausted.
Return dummy.next (skipping dummy head).
Key Concepts Used:
Linked List traversal
Carry handling in addition
Dummy node to avoid edge-case handling
Time Complexity: O(max(m, n)) – where m and n are the lengths of l1 and l2.
Space Complexity: O(max(m, n)) – result stored as a new linked list."""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        carry=0
        while l1 or l2 or carry:
            val1=l1.val if l1 else 0
            val2=l2.val if l2 else 0
            tot=val1+val2+carry
            carry=tot//10
            dig=tot%10
            curr.next=ListNode(dig)
            curr=curr.next
            if l1:l1=l1.next
            if l2:l2=l2.next
        return dummy.next