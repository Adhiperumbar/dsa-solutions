"""
Date: 06-09-2025
Problem: Maximum Sum Circular Subarray (LeetCode 918)
Problem Statement:
Given a circular integer array nums, return the maximum possible sum of a non-empty subarray. The subarray may wrap around (i.e., connect the end of the array to the beginning).
Approach:
Use a modified version of Kadane’s Algorithm to track both maximum and minimum subarray sums.
currentmax, maxsum → track maximum subarray sum.
currentmin, minsum → track minimum subarray sum.
For each element:
Update currentmax = max(nums[i], currentmax + nums[i]).
Update maxsum = max(maxsum, currentmax).
Update currentmin = min(nums[i], currentmin + nums[i]).
Update minsum = min(minsum, currentmin).
Special Case:
If all numbers are negative, return maxsum (since sum(nums) - minsum would be zero).
Otherwise, return max(maxsum, sum(nums) - minsum) to cover both normal and circular subarrays.
Key Concepts Used:
Kadane’s Algorithm
Circular array handling
Edge case check (all negatives)
Time Complexity: O(n) – single traversal of the array
Space Complexity: O(1) – constant variables used
"""
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentmax=maxsum=nums[0]
        currentmin=minsum=nums[0]
        for i in range(1,len(nums)):
            currentmax=max(nums[i],currentmax+nums[i])
            maxsum=max(currentmax,maxsum)
            currentmin=min(nums[i],currentmin+nums[i])
            minsum=min(currentmin,minsum)
        if maxsum<0:
            return maxsum
        return max(maxsum,sum(nums)-minsum)