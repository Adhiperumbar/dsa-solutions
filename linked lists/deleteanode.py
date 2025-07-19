"""✅ Problem: Delete Node in a Linked List  
🔗 LeetCode: https://leetcode.com/problems/delete-node-in-a-linked-list/  
📅 Date Solved: 19-07-2025  
🧠 Approach: In-Place Node Overwrite  
📝 Notes:
- The node to be deleted is **not the tail**, and we are **not given head**.
- So instead of traditional deletion, I:
  - Copied the next node’s value into the current node.
  - Then bypassed the next node using `node.next = node.next.next`.
- This effectively "deletes" the given node by overwriting it.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val=node.next.val
        node.next=node.next.next
        
        