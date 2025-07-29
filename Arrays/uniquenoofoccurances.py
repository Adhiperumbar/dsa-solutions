"""✅ Problem: Unique Number of Occurrences  
🔗 LeetCode: https://leetcode.com/problems/unique-number-of-occurrences/  
🗓️ Date Solved: 29-07-2025  
🧠 Approach: Frequency Map + Set  
📝 Notes:  
Goal: Check whether the number of times each element appears in the array is unique.  
Built a frequency dictionary `{element: count}` using a loop.  
Used `set(values)` to get distinct frequencies.  
If the number of unique frequencies equals the number of unique elements, return True.  
✅ Time: O(n), ✅ Space: O(n)  
A classic hashmap + set check for uniqueness!
"""
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s={}
        for i in range(len(arr)):
            if arr[i] in s :
                s[arr[i]]+=1
            else:
                s[arr[i]]=1
        k=set(s.values())
        if len(k)==len(s):
            return True
        else:
            return False