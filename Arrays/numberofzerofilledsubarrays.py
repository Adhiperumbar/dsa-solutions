"""
Problem: Number of Zero-Filled Subarrays (LeetCode 2348)
Problem Link: https://leetcode.com/problems/number-of-zero-filled-subarrays
Date Solved: 19-08-2025
Approach: Counting Consecutive Zeros
Iterate through the array while tracking consecutive zeros (count).
When a non-zero appears, calculate subarrays from the streak:
subarrays=count×(count+1)
Reset count and continue.
At the end, add contribution of the last streak.
Complexity:
Time: O(n) (single pass)
Space: O(1) (only counters used)
"""
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count=0
        res=0
        for i in nums:
            if i==0:
                count+=1
            else:
                res+=(count*(count+1))//2
                count=0
        res+=(count*(count+1))//2
        return res
            