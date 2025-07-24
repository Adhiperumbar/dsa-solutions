"""✅ Problem: Greatest Common Divisor of Strings
🔗 LeetCode: https://leetcode.com/problems/greatest-common-divisor-of-strings/
🗓️ Date Solved: 24-07-2025
🧠 Approach: String Concatenation Check + Euclidean Algorithm
📝 Notes:
First, checked if str1 + str2 == str2 + str1. If not, there’s no common base string, so returned "".
If the check passed, used the Euclidean algorithm to find the GCD of the lengths of both strings.
Returned the substring of str1 from 0 to gcd(length1, length2) as the answer."""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1+str2!= str2+str1:
            return ""
        a=len(str1)
        b=len(str2)
        while b!=0:
            temp=b
            b=a%b
            a=temp
        return str1[0:a]