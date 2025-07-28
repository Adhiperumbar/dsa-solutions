# Date Solved: 28/07/2025
# Problem: Maximum Number of Vowels in a Substring of Given Length (LeetCode)
# Approach: Sliding Window
# - Count vowels in the first window of size k
# - Slide the window forward by adding one char and removing one from the left
# - Update the count efficiently and keep track of max
# Time Complexity: O(n), Space: O(1)
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        mx=0
        c=0
        vowels = set('aeiou')
        for i in range(k):
            if s[i] in vowels:
                c+=1
            mx=c
        for i in range(k,len(s)):
            if s[i] in vowels:
                c+=1
            if s[i-k] in vowels:
                c-=1
            mx=max(mx,c)
        return mx
