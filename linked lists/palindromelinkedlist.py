"""✅ Problem: Palindrome Linked List
🔗 LeetCode: https://leetcode.com/problems/palindrome-linked-list/
🗓️ Date Solved: 19-07-2025
🧠 Approach: Two Pointers + Reverse Second Half
📝 Notes:
Used slow and fast pointers to reach the middle of the linked list.
Reversed the second half of the list in-place.
Compared the first half and the reversed second half node-by-node.
If any mismatch is found, return False; otherwise, it's a palindrome.
No extra space used — O(n) time and O(1) space.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        prev=None
        cur=slow
        while cur:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        left=head
        right=prev
        while  right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True