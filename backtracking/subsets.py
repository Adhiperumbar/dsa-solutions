"""✅ Problem: Subsets
🔗 LeetCode Link
🗓️ Date Solved: 21-07-2025
🧠 Approach: Backtracking (Recursive)
📁 Category: Recursion / Subsets / Backtracking
⚙️ Time Complexity: O(2^n)
🧮 Space Complexity: O(n) (path size during recursion)
💡 What I Learned:
Used backtracking to generate all possible subsets.
At each index, chose to either include or exclude an element.
Used path[:] to store a copy of current path, not reference (to avoid mutation issues).
Added subsets to the result list s at every recursive level.
Used path.pop() to backtrack after recursive call.
❌ Mistakes I Made:
Initially forgot to append a copy (path[:]) instead of path directly.
Got confused with recursive index management — learned i+1 keeps track of the next element to explore.
Also missed backtracking (pop()) in first attempts.
Understood how recursion tree expands and why order matters."""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        s=[]
        def backtrack(index,path):
            s.append(path[:])
            for i in range(index,len(nums)):
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return s