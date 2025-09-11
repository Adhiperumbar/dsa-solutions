"""
Date: 11-09-2025
Problem: Linked List Cycle (LeetCode 141)
Problem Statement:
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if some node can be reached again by continuously following the next pointer.
Approach (Floyd’s Cycle Detection / Tortoise and Hare):
Use two pointers:
slow → moves one step at a time.
fast → moves two steps at a time.
Traverse the list:
If at any point fast == slow, a cycle is detected.
If fast or fast.next becomes None, the list ends and no cycle exists.
Key Concepts Used:
Floyd’s Cycle Detection Algorithm
Two-pointer technique
Time Complexity: O(n) – at most one full traversal of the list.
Space Complexity: O(1) – constant space used.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast=head
        slow=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return True
        return False
        