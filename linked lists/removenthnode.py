"""
✅ Problem: Remove Nth Node From End of List  
🔗 LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
📅 Date Solved: 19-07-2025  
🧠 Approach: Two-Pass Traversal  
📝 Notes:
- First, I traversed the list once to count the total number of nodes (`count`).
- Then I calculated the position from the start: `count - n`.
- If the node to be removed is the head, return `head.next`.
- Otherwise, traversed again to the node just before the one to be deleted.
- Skipped the `nth` node using: `cur.next = cur.next.next`.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur=head
        count=0
        while cur:
            cur=cur.next
            count+=1
        count=count-n
        if count==0:
            return head.next
        cur=head
        for i in range(count-1):
            cur=cur.next
        cur.next=cur.next.next
        return head

