"""
Date: 07-10-2025
Problem Name: Reverse Integer
Leetcode Link: https://leetcode.com/problems/reverse-integer
Platform: LeetCode
Difficulty: Medium
Language Used: Python

Problem Statement:
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range 
[-2^31, 2^31 - 1], then return 0.

Examples:
Input: x = 123  → Output: 321
Input: x = -123 → Output: -321
Input: x = 120  → Output: 21

Approach (String Construction + Manual Reversal):
- Take the absolute value of x to handle both positive and negative cases uniformly.
- Initialize an empty string s.
- Extract the last digit of n using n % 10 and add it to s.
- Update n = n // 10 to remove the last digit.
- Continue until n becomes 0.
- Convert the string s back to an integer.
- If the original number x was negative, make the result negative.
- Return 0 if the reversed integer is outside the 32-bit signed range.

Time Complexity:
- O(log₁₀ n), since each iteration removes one digit.

Space Complexity:
- O(log₁₀ n), to store the digits as characters in the string.

What I Learned:
- Handling integer reversal safely requires considering 32-bit overflow.
- It’s important to preserve the original sign before modifying x.
- String concatenation can make reversal easy, but pure math solutions are more optimal.
"""
class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        s = ""
        while n > 0:
            k = n % 10
            n = n // 10
            s += str(k)
        
        if s == "":
            return 0

        if int(s) < -2**31 or int(s) > 2**31 - 1:
            return 0
        
        if x < 0:
            return -int(s)
        return int(s)
