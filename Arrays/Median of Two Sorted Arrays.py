# Problem: Median of Two Sorted Arrays (LeetCode 4)
# Solved on: 10-07-2025
# Approach: Brute-force – merge, sort, then find median
# Notes: Initially averaged indices instead of values (k + l). Realized it must be (num[k-1] + num[k])/2.
# Plan: Revisit this later with the O(log(min(m, n))) optimized solution.

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num=nums1+nums2
        num.sort()
        n=len(num)
        k=int(n/2)
        if n%2==0:
            med=(num[k-1]+num[k])/2
            return med
        else:
            return num[k]