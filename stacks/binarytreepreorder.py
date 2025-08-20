"""
✅ Problem: 144. Binary Tree Preorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-preorder-traversal/
🗓️ Date Solved: 21-08-2025
🧠 Approach: Iterative Preorder Traversal using Stack
Preorder traversal follows Root → Left → Right order.
Used a stack to simulate recursion.
Start by pushing the root node into the stack.
At each step:
Pop the node, process it (res.append(node.val)),
Push the right child (if any), then the left child (if any) → ensures left is processed first.
⏱️ Time Complexity: O(n) – each node is visited once.
💾 Space Complexity: O(n) – in the worst case (skewed tree), the stack holds all nodes.
✅ Key Learning
Preorder traversal can be done iteratively by pushing nodes in reverse order (right before left) to maintain correct processing order. This avoids recursion and works efficiently for large trees.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[]
        if root:
            stack.append(root)
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res