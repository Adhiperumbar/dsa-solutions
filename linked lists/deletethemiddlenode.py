"""✅ Problem: Delete the Middle Node of a Linked List
🔗 LeetCode: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
🗓️ Date Solved: 25-07-2025
🧠 Approach: Two-pass Linked List Traversal
📝 Notes:
Handled edge cases where list is empty or has only one node.
First traversal to count total nodes (n).
Middle index calculated as n // 2.
Second traversal to reach node before middle.
Adjusted pointers to skip the middle node.
Returned modified linked list head.
Simple but requires two traversals.
Optimization possible using slow and fast pointers to achieve one pass.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if not head or not head.next:
            return None
        n=0
        while cur:
            cur=cur.next
            n+=1
        n=n//2
        cur=head
        for i in range(n-1):
            cur=cur.next
        cur.next=cur.next.next
        return head       