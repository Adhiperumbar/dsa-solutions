"""Problem: Check Divisibility by Sum + Product of Digits
Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
📅 Date Solved: 30-07-2025
🧠 Approach: Digit Extraction + Arithmetic
📄 Description:
Given an integer n, check whether it is divisible by the sum of its digits plus the product of its digits.
📝 Notes:
Extracted each digit using modulo (% 10) and integer division (// 10).
Maintained two accumulators: digit_sum and digit_prod.
Added both to get total.
Final check: n % total == 0
Carefully avoided variable names like sum and prod to prevent overriding Python built-ins.
✅ Time Complexity: O(log₁₀n)
✅ Space Complexity: O(1)"""
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        t = n
        digit_sum = 0
        digit_prod = 1
        while t > 0:
            d = t % 10
            digit_sum += d
            digit_prod *= d
            t //= 10
        total = digit_sum + digit_prod
        return n % total == 0
