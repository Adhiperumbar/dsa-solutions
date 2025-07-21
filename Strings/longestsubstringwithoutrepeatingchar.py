"""✅ Problem: Longest Substring Without Repeating Characters  
🔗 LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/  
📅 Date Solved: 21-07-2025  
🧠 Approach: Sliding Window with HashSet  
📝 Notes:
- Used a `set` to store unique characters in the current window.
- Used two pointers (`left` and `right`) to manage the window.
- If a duplicate character is found at `s[right]`, move the `left` pointer and remove characters from the set until it's unique again.
- After each iteration, update `maxlen` with the size of the current valid window.
- Time Complexity: O(n), Space Complexity: O(n)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen=set()
        left=0 
        maxlen=0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[right])
            maxlen=max(maxlen,right-left+1)
        return maxlen