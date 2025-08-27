"""
✅ Problem: House Robber II (Circular Houses)
🔗 LeetCode: https://leetcode.com/problems/house-robber-ii/
🗓️ Date Solved: [fill your date]
🧠 Approach: Dynamic Programming + Two Variables
Since the houses are circular, the first and last house cannot both be robbed
Defined a helper function robb to solve the linear version (House Robber I) using two variables
rob1 → maximum up to previous house
rob2 → maximum up to house before previous
For each house value
new = max(rob1, rob2 + num)
Update rob2 = rob1, rob1 = new
Solved two cases separately:
Rob houses from first to second-last (nums[:-1])
Rob houses from second to last (nums[1:])
Returned the maximum of the two cases.
💡 Key Points:
Reduces the circular problem to two linear subproblems.
Optimized O(1) space by using only two variables.
Works for empty lists or single-house cases.
⏱ Complexity:
Time: O(n) — iterates through each sublist once.
Space: O(1) — only a few variables used, no extra data structures.
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        def robb(nums:List[int])->int:
            rob1=0
            rob2=0
            for num in nums:
                new=max(rob1,rob2+num)
                rob2=rob1
                rob1=new
            return rob1
        case1=robb(nums[:-1])
        case2=robb(nums[1:])
        return max(case1,case2)
