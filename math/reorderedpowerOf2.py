"""
Date: 10-08-2025
Problem Name: Reordered Power of 2
Leetcode Link: https://leetcode.com/problems/reordered-power-of-2
Platform: LeetCode
Difficulty: Medium
Language Used: Python
Problem Statement:
Given an integer n, return True if we can reorder the digits of n to form a power of two, and False otherwise. Reordering of digits includes not changing them at all.
Approach:
Convert n to a string and sort its digits to get the target arrangement.
Iterate over all powers of two from 2^0 to 2^30 (since 2^30 is the largest power of two within 10 digits).
Convert each power of two to a string, sort its digits, and compare with the target.
If any match is found, return True.
If no match is found after the loop, return False.
Time Complexity:
O(k log k) for sorting digits, where k is the number of digits in the number.
Since we loop 31 times, overall complexity is O(31 * k log k) → practically constant.
Space Complexity:
O(k) for storing the sorted digits.
What I Learned:
Powers of two have a very limited range for integers up to 10 digits, so brute-forcing all powers of two is efficient.
Using sorted(str(num)) is a quick way to compare permutations of digits."""

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        target = sorted(str(n))
        for i in range(31):
            if sorted(str(1 << i)) == target:
                return True
        return False