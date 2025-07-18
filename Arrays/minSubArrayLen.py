"""# ✅ Problem: Minimum Size Subarray Sum
# 🔗 LeetCode: https://leetcode.com/problems/minimum-size-subarray-sum/
# 🗓️ Date Solved: 18-07-2025
# 🧠 Approach: Sliding Window
# 📝 Notes:
# - I used a variable `start` to track the start of the sliding window.
# - For each `end`, I add the value to `sum`.
# - If `sum >= target`, I try to shrink the window from the left.
# - Track the minimum window length.
# - Return 0 if no valid subarray found.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start=0
        min_len = float('inf')
        sum=0
        for end in range(len(nums)):
            sum += nums[end]
            while sum >= target:
                min_len = min(min_len, end + 1 - start)
                sum -= nums[start]
                start += 1
        return 0 if min_len == float('inf') else min_len
