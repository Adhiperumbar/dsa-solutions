"""
✅ Problem: Maximum Subarray
🔗 LeetCode: 53. Maximum Subarray
🗓️ Date Solved: 30-08-2025
🧠 Approach: Kadane’s Algorithm (Dynamic Programming)
Maintained two variables:
cs → current maximum subarray sum ending at current index
ms → overall maximum subarray sum found so far
For each element nums[i]:
cs = max(nums[i], cs + nums[i]) → either start new subarray or extend current one
ms = max(ms, cs) → update overall maximum
Returned ms as the maximum subarray sum.
💡 Key Points:
Efficient O(n) time solution using O(1) space.
Handles negative numbers and all-positive arrays.
Simple iteration with dynamic updating of sums.
⏱ Complexity:
Time: O(n) — single pass through the array.
Space: O(1) — only two variables used.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms=nums[0]
        cs=nums[0]
        for i in range(1,len(nums)):
            cs=max(nums[i],cs+nums[i])
            ms=max(ms,cs)
        return ms