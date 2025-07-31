"""Problem: Close Strings
Platform: LeetCode
Date Solved: 30-07-25
Topic: Hashing / Frequency Counter
Approach:
First check if both strings have the same set of characters.
Then compare the sorted frequency values of both strings.
This ensures the strings are "close" under the problem's allowed operations."""

from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        s = set(word1)
        t = set(word2)
        if s != t:
            return False
        freq1 = Counter(word1)
        freq2 = Counter(word2)
        return sorted(freq1.values()) == sorted(freq2.values())
