"""
✅ Problem: Binary Tree Inorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal   
🗓️ Date Solved: 20-08-2025
🧠 Approach: Iterative Inorder Traversal using Stack
Used a stack to simulate the recursive behavior of inorder traversal.
Keep pushing nodes while going left, then pop, process value, and move right.
This avoids recursion and handles large trees efficiently.
📜 Key Steps:
Initialize stack = [] and cur = root.
Traverse left until cur is None, pushing nodes to stack.
Pop node from stack, add its value to res.
Move to right child and repeat until both stack and cur are empty.
⏱️ Complexity:
Time: O(n) (every node is pushed and popped once).
Space: O(n) (stack in worst case when tree is skewed).
💡 Learning:
Iterative inorder traversal is a great alternative to recursion.
Helped me understand how recursion works under the hood by mimicking the call stack manually.
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack=[]
        res=[]
        cur=root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur=cur.left
            cur=stack.pop()
            res.append(cur.val)
            cur=cur.right
        return res
