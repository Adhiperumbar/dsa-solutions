"
✅ Problem: Largest 3-Same-Digit Number in String
🔗 LeetCode: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
🗓️ Date Solved: 14-08-2025
🧠 Approach: Sliding Window (size = 3)
I used a fixed-size sliding window to check every triplet in the string. For each window, if all three digits were the same, I compared it with my current maximum. Since the input remains a string, direct lexicographic comparison worked. Learned the importance of avoiding unnecessary list() conversion in string problems — it broke comparisons earlier by turning slices into lists. Also, remembered not to shadow built-in functions like max."
Code:
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_digit = ""
        for i in range(len(num) - 2):
            window = num[i:i+3]
            if window[0] == window[1] == window[2]:
                if window > max_digit:
                    max_digit = window
        return max_digit
