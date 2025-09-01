"""
Date: 01-09-2025
Problem: Add Binary
Problem Statement:
Given two binary strings a and b, return their sum as a binary string.
Approach:
Start from the last index of both strings (i for a, j for b).
Maintain a variable c for carry and a list res for storing result digits.
Loop while i >= 0 or j >= 0 or there is a carry.
Initialize t with the carry.
If i >= 0, add a[i] to t and move i left.
If j >= 0, add b[j] to t and move j left.
Append t % 2 (binary digit) to res.
Update c = t // 2.
Reverse the result list and join to form the final binary string.
Key Concepts Used:
Two pointer approach (right to left).
Carry handling in binary addition.
String manipulation and reversing.
Time Complexity: O(n) (where n = max(len(a), len(b)))
Space Complexity: O(n) (for the result list).
"""
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i=len(a)-1
        j=len(b)-1
        res=[]
        c=0
        while i>=0 or j>=0 or c:
            t=c
            if i>=0:
                t+=int(a[i])
                i-=1
            if j>=0:
                t+=int(b[j])
                j-=1
            res.append(str(t%2))
            c=t//2
        return "".join(reversed(res))