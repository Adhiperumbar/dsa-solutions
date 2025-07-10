# Problem: Two Sum (LeetCode 1)
# Solved on: 10-07-2025
# Approach: Brute-force with nested loops
# Notes: First few attempts had index logic issues. Got it working after reviewing pairs.
# Plan: Try using a hash map for O(n) solution next.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return [i,j]
        return "null"