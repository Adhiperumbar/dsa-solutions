"
✅ Problem: Maximum 69 Number
🔗 LeetCode: https://leetcode.com/problems/maximum-69-number/
🗓️ Date Solved: 17-08-2025
🧠 Approach: String Replacement
The problem asks to maximize a number made of digits 6 and 9 by changing at most one digit. The greedy choice is to change the first occurrence of 6 into 9, since that affects the highest place value. I solved it by converting the integer to a string, replacing the first '6' with '9', and converting it back to int. This is both concise and efficient.
Complexities:
⏱ Time Complexity: O(d) where d is the number of digits in num (string conversion + replace + int conversion).
📦 Space Complexity: O(d) for storing the string representation of num.
"
Code:

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))
