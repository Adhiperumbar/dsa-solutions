"
✅ Problem: Power of Four
🔗 LeetCode: https://leetcode.com/problems/power-of-four/
🗓️ Date Solved: 15-08-2025
🧠 Approach: Iterative Division
I checked if n is a positive number first. Then, I repeatedly divided n by 4 as long as it was divisible by 4. If the final result equals 1, then n is a power of four. This approach is simple, avoids floating-point issues, and has logarithmic complexity.
"
Code:
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1
