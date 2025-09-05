"""
Date: 05-09-2025
Problem: Climbing Stairs (LeetCode 70)
Problem Statement:
You are climbing a staircase with n steps. You can take either 1 or 2 steps at a time. Return the number of distinct ways to reach the top.
Approach:
Handle base cases:
If n == 1, return 1.
If n == 2, return 2.
Use dynamic programming to store the number of ways to reach each step:
Initialize dp array of size n.
dp[0] = 1 → 1 way to reach step 1.
dp[1] = 2 → 2 ways to reach step 2.
For each step i from 2 to n-1:
dp[i] = dp[i-1] + dp[i-2] → ways to reach step i = sum of ways to reach previous two steps.
Return dp[n-1] as the total number of ways.
Key Concepts Used:
Dynamic Programming
Fibonacci sequence pattern
Time Complexity: O(n) – single pass to fill DP array
Space Complexity: O(n) – DP array of size n

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        if n==2:
            return 2
        dp=[0]*n
        dp[0]=1
        dp[1]=2
        for i in range(2,n):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n-1]

#OPTIMIZED SPACE:
 

class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        a=1
        b=2
        for i in range(2,n):
            a,b=b,a+b
        return b