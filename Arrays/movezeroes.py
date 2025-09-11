"""
Date: 11-09-2025
Problem: Move Zeroes (LeetCode 283)
Problem Statement:
Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. The operation must be done in-place without making a copy of the array.
Approach:
Use a two-pointer technique:
o → tracks the position where the next non-zero element should go.
i → iterates through the array.
If nums[i] is non-zero, swap it with nums[o] and increment o.
By the end of traversal, all non-zeros are at the front in order, and zeros are pushed to the back.
Key Concepts Used:
Two-pointer method
In-place swapping
Time Complexity: O(n) – traverses the list once.
Space Complexity: O(1) – constant extra space.
"""
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=len(nums)
        o=0
        for i in range(k):
            if nums[i]!=0:
                nums[i],nums[o]=nums[o],nums[i]
                o+=1
        