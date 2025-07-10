# Problem: First Unique Character in a String (LeetCode 387)
# Solved on: 09-07-2025
# Approach: Frequency count, then linear scan
# Notes: Learned that order of operations matters — count first, then index check.
# Plan: Could try doing it in one pass with a queue.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for x in range(len(s)):
            count[s[x]] = count.get(s[x], 0) + 1
        for x,char in enumerate(s):
            if count[s[x]] == 1:
                return x
        return -1
