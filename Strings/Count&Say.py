"""
✅Problem: Count and Say
🔗LeetCode: 38. Count and Say
🗓️Date Solved: 31-08-2025
🧠Approach: Iterative String Construction
Start with res="1".
For each iteration up to n: traverse res, count consecutive identical digits, build temp="<count><digit>", then update res=temp.
Return res after n iterations.
💡Key Points:
Nested loops count consecutive characters.
Builds next term iteratively without recursion.
Works for all n≥1.
⏱Complexity:
Time: O(2ⁿ)
Space: O(2ⁿ)
"""
class Solution:
    def countAndSay(self, n: int) -> str:
        res="1"
        for k in range(1,n):
            temp=""
            i=0
            while i<len(res):
                c=1
                while i+1<len(res) and res[i]==res[i+1]:
                    i+=1
                    c+=1
                temp+=str(c)+res[i]
                i+=1
            res=temp
        return res