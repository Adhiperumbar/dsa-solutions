"""
Date: 06-09-2025
Problem: Maximum Product Subarray (LeetCode 152)
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest product, and return that product.
Approach:
This is similar to Maximum Subarray Sum, but products behave differently due to negative numbers.
At each index i, track two values:
cmax: the maximum product ending at i.
cmin: the minimum product ending at i.
Reason: a negative number can flip min ↔ max.
If nums[i] is negative, swap cmax and cmin.
Update:
cmax = max(nums[i], cmax * nums[i])
cmin = min(nums[i], cmin * nums[i])
Track the result:
res = max(res, cmax)
Key Concepts Used:
Dynamic Programming (Kadane’s variant)
Handling negative numbers by maintaining both min & max
Greedy updating in one pass
Time Complexity: O(n) – iterate once through nums
Space Complexity: O(1) – constant extra space
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cmin=cmax=res=nums[0]
        for i in range(1,len(nums)):
            n=nums[i]
            if n<0:
                cmax,cmin=cmin,cmax
            cmax=max(n,cmax*n)
            cmin=min(n,cmin*n)
            res=max(res,cmax)
        return res