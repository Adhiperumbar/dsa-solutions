"""
Date: 05-09-2025
Problem: Fibonacci Number (LeetCode 509)
Problem Statement:
Given n, return the nth Fibonacci number. The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Approach (Dynamic Programming):
Handle base cases:
If n == 0, return 0
If n == 1, return 1
Initialize a DP array dp of size n+1.
dp[0] = 0
dp[1] = 1
For each i from 2 to n:
dp[i] = dp[i-1] + dp[i-2] → store the Fibonacci value at i.
Return dp[n] as the nth Fibonacci number.
Key Concepts Used:
Dynamic Programming
Bottom-up computation of Fibonacci numbers
Time Complexity: O(n) – single pass through the array
Space Complexity: O(n) – DP array of size
"""
#code:
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]


#Optimised Space Complexity O(1):
"""
Approach (Space-Optimized):
Handle base cases:
If n == 0, return 0
If n == 1, return 1
Use two variables a and b to store the previous two Fibonacci numbers:
a = 0 → F(0)
b = 1 → F(1)
For each i from 2 to n:
Update a, b = b, a + b → shift previous values and compute current Fibonacci number.
Return b as the nth Fibonacci number.
Key Concepts Used:
Dynamic Programming / Fibonacci sequence
Space optimization using two variables
Time Complexity: O(n) – iterate through 2 to n
Space Complexity: O(1) – only two variables used
"""

class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        a=0
        b=1
        for i in range(2,n+1):
            a,b=b,a+b
        return b