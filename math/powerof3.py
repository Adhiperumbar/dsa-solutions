"""
Date: 13-08-2025
Problem Name: Power of Three
Leetcode Link: https://leetcode.com/problems/power-of-three
Platform: LeetCode
Difficulty: Easy
Language Used: Python
Problem Statement:
Given an integer n, return True if it is a power of three. Otherwise, return False.
An integer n is a power of three if there exists an integer k such that n == 3^k.
Approach 1 (Iterative Division):
- If n < 1, return False (negative numbers and zero are not powers of three).
- While n is divisible by 3 (n % 3 == 0), divide n by 3.
- After the loop, if n == 1, return True; otherwise, return False.
Approach 2 (Backtracking):
- Define a recursive function starting from current = 1.
- At each step:
    - If current == n, return True.
    - If current > n, return False.
    - Multiply current by 3 and recurse.
- Start the recursion with current = 1.
Time Complexity:
- Both approaches take O(log₃ n) time because we divide or multiply by 3 each step.
Space Complexity:
- Iterative: O(1) extra space.
- Backtracking: O(log₃ n) recursion stack space.
What I Learned:
- For checking powers of a number, repeated division or multiplication is a straightforward method.
- Backtracking can work here but is unnecessary unless the problem naturally involves exploring multiple possibilities.
- Iterative division is more space-efficient and cleaner for this problem.
"""
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def backtrack(current):
            if current==n:
                return True
            if current>n:
                return False 
            return backtrack(current*3)
        return backtrack(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<1:
            return False
        while n%3==0:
            n=n//3
        return n==1