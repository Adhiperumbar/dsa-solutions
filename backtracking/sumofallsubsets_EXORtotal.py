"""✅ Problem: Subset XOR Sum
🔗 LeetCode Link
🗓️ Date Solved: 23-07-2025
🧠 Approach: Backtracking
📁 Category: Recursion / Bit Manipulation / Subsets
⚙️ Time Complexity: O(2^n) — where n is the number of elements in nums
🧮 Space Complexity: O(n) — recursive stack depth
💡 What I Learned:
Used backtracking to explore all possible subsets.
At each step, made a choice to include or exclude the current element using XOR.
Maintained a total variable to accumulate the XOR values of all subsets.
Used nonlocal to modify the outer total variable from inside the nested function.
❌ Mistakes I Made:
Initially forgot to use nonlocal total, which caused the variable to not update as expected.
Also missed the base case where index == len(nums) to trigger accumulation.
Needed time to understand how XOR works over subsets, especially how ^ behaves."""

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total=0
        def backtrack(index,currentxor):
            nonlocal total
            if index==len(nums):
                total += currentxor
                return
            backtrack(index+1,currentxor^nums[index])
            backtrack(index+1,currentxor)
        backtrack(0,0)
        return total