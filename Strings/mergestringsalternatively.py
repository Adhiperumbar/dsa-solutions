"""✅ Problem: Merge Strings Alternately
🔗 LeetCode: https://leetcode.com/problems/merge-strings-alternately/
🗓️ Date Solved: 24-07-2025
🧠 Approach: Index-Based Merging Using Lists
📝 Notes:
Converted both strings into lists to access characters by index.
Used a loop running up to the length of the longer word.
Added characters from each word if the index was within bounds.
Used ''.join(s) to convert the final list of characters into a merged string.
Also handled edge cases like empty input strings."""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        wo1=list(word1)
        wo2=list(word2)
        a=len(wo1)
        b=len(wo2)
        s=[]
        if a ==0 and b==0:
            return str(s)
        for i in range(max(a,b)):
            if i<a:
                s.append(wo1[i])
            if i<b:
                s.append(wo2[i])
        return ''.join(s)
