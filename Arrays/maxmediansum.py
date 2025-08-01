"""Problem: Maximum Median Sum
Link: https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/description/
📅 Date Solved: 01-08-2025
🧠 Approach: Greedy + Sorting
📄 Description:
Given an array of integers nums with length n = 3k, divide the array into k groups of 3 elements.
From each group, select the median (2nd largest element), and maximize the sum of these medians.
📝 Notes:
Sorted the array in ascending order.
To maximize the total median sum, chose every 2nd largest element from the last 3k elements.
Specifically, picked elements at positions: n-2, n-4, ..., down to n//3.
This strategy works because by choosing the top 3k numbers and carefully skipping one largest and one smallest per group, we can greedily pick the optimal medians.
✅ Time Complexity: O(n log n)
✅ Space Complexity: O(1)"""
class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        t=0
        for i in range (n-2,n//3 -1,-2):
            t+=nums[i]
        return t
            