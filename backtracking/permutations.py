"""
✅ Problem: Permutations
🔗 LeetCode Link
🗓️ Date Solved: 23-07-2025
🧠 Approach: Backtracking
📁 Category: Backtracking / Recursion
⚙️ Time Complexity: O(n * n!)
🧮 Space Complexity: O(n) for the recursive call stack
💡 What I Learned:
Used a backtracking approach to generate all permutations.
Created a helper function backtrack(path) where path stores the current permutation.
Used if len(path) == len(nums) to check for completion of one permutation.
Appended a copy of path using path[:] to avoid reference issues.
❌ Mistakes I Made:
Initially unsure how to prevent repeated elements in a permutation — fixed by checking if nums[i] not in path.
Forgot that path.append() mutates the list, so used path.pop() correctly after the recursive call to backtrack.
Slight confusion with how recursion unwinds, but understood it after tracing with small inputs."""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        s=[]
        def backtrack(path):
            if len(path)==len(nums):
                        s.append(path[:])
            for i in range(len(nums)):
                if nums[i] not in path:
                    path.append(nums[i])
                    backtrack(path)
                    path.pop()
        backtrack([])
        return s