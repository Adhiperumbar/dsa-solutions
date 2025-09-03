"""
Date: 03-09-2025
Problem: Find the Index of the First Occurrence in a String
Problem Statement:
Given two strings haystack and needle, return the index of the first occurrence of needle in haystack. If needle is not part of haystack, return -1.
Approach:
Loop from i = 0 to len(haystack) - len(needle).
For each index, take the substring haystack[i : i + len(needle)].
If the substring equals needle, return the index i.
If no match is found after the loop, return -1.
Key Concepts Used:
String slicing
Brute force substring search
Time Complexity: O((n - m + 1) * m), where n = len(haystack) and m = len(needle)
Space Complexity: O(1)
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(0,len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return-1