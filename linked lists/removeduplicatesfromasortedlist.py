"""✅ Problem: Remove Duplicates from Sorted Linked List
🔗 LeetCode: 83. Remove Duplicates from Sorted List
🗓️ Date Solved: [fill your date]
🧠 Approach: HashSet + Iteration
Used a visited set to store unique values while traversing the linked list.
Maintained two pointers:
cur → current node
prev → last unique node
If the current node’s value is already in visited, skipped it by updating prev.next.
Otherwise, added it to visited and moved prev forward.
💡 Key Points:
Works for both sorted and unsorted linked lists.
Uses O(n) extra space for the set.
Alternative: For sorted lists, you can solve it in-place with O(1) space by skipping duplicates directly.
⏱ Complexity:
Time: O(n) — traverses the list once.
Space: O(n) — extra space for the visited set."""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
         visited=set()
         cur=head
         prev=None
         while cur:
            if cur.val in visited:
                prev.next=cur.next
            else:
                visited.add(cur.val)
                prev=cur
            cur=cur.next
         return head