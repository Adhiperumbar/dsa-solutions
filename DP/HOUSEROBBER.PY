"""
✅ Problem: House Robber
🔗 LeetCode Link: [198. House Robber] https://leetcode.com/problems/house-robber/ 
🗓️ Date Solved: 26-08-2025
🧠 Approach: Dynamic Programming (Optimized with Two Variables)
Maintained two variables:
rob1 → maximum amount robbed up to the previous house
rob2 → maximum amount robbed up to the house before the previous one
For each house value num:
Calculated new_rob = max(rob1, rob2 + num)
Updated rob2 = rob1 and rob1 = new_rob
Returned rob1 as the maximum amount that can be robbed.
💡 Key Points:
Optimized solution using O(1) space instead of a full DP array.
Simple and clean iteration, only updating two variables.
Works for any list of non-negative house values.
⏱ Complexity:
Time: O(n) — iterates through the list once.
Space: O(1) — only two extra variables used.
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1=0
        rob2=0
        for num in nums:
            new_rob=max(rob1,rob2+num)
            rob2=rob1
            rob1=new_rob
        return rob1
