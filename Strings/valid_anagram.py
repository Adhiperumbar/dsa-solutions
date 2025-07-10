# Problem: Valid Anagram (LeetCode 242)
# Solved on: 09-07-2025
# Approach: Frequency count using a list of size 26
# Notes: Solidified understanding of character indexing (ord trick). Simple but useful.
# Plan: Try using `collections.Counter` for comparison in one line.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charlist=[0]*26
        for i in s:
            index=ord(i)-ord('a')
            charlist[index]+=1
        for i in t:
            index=ord(i)-ord('a')
            charlist[index]-=1
            return charlist!=[0]*26
            