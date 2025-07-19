"""✅ Problem: Reverse Linked List
🔗 LeetCode: https://leetcode.com/problems/reverse-linked-list/
🗓️ Date Solved: 19-07-2025
🧠 Approach: Iterative Reversal
📝 Notes:

Used two pointers prev and cur to reverse the list in-place.

At each step, saved the next node and redirected cur.next to prev.

Updated pointers until reaching the end of the list.

Returned prev, which becomes the new head of the reversed list.

Time Complexity: O(n)

Space Complexity: O(1)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        prev=None
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        return prev