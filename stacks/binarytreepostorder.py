"""
✅ Problem: 145. Binary Tree Postorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-postorder-traversal/
🗓️ Date Solved: 21-08-2025
🧠 Approach: Iterative Postorder Traversal using Two Stacks
Postorder traversal follows Left → Right → Root order.
Used two stacks to simulate recursion and reverse the node processing order.
Start by pushing the root node into the first stack.
At each step:
Pop a node from the first stack and push its value to the second stack.
Push the left child (if any), then the right child (if any) into the first stack.
After processing all nodes, pop all values from the second stack to get the postorder sequence.
⏱️ Time Complexity: O(n) – each node is visited once.
💾 Space Complexity: O(n) – in the worst case, both stacks hold all nodes.
✅ Key Learning:
Postorder traversal can be implemented iteratively by reversing the processing order of a modified preorder traversal (Root → Right → Left) using two stacks. This method provides a clear and efficient way to perform postorder traversal without recursion.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        stack=[root]
        stack2=[]
        if not root:
            return []
        while stack:
            node=stack.pop()
            stack2.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while stack2:
            node=stack2.pop()
            res.append(node)
        return res