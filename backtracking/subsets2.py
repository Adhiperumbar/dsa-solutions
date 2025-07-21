"""✅ Problem: Subsets II
🔗 LeetCode Link
🗓️ Date Solved: 21-07-2025
🧠 Approach: Backtracking with Duplicate Handling
📁 Category: Recursion / Backtracking / Subsets
⚙️ Time Complexity: O(2^n)
🧮 Space Complexity: O(n) (depth of recursive stack)
💡 What I Learned:
Used backtracking to generate all possible subsets even with duplicates.
Sorted the array to group duplicates together, which helped in skipping repeated branches.
The line if nums[i] == nums[i - 1] and i > index: ensures we skip duplicate elements only if they are not the first element at that level.
Added path[:] to result for a copy of current state.
Practiced how pruning the recursion tree reduces duplicate combinations.
❌ Mistakes I Made:
Initially forgot to sort the array, which caused duplicate subsets to appear.
Didn't understand the condition i > index — now I know it helps control tree-level duplicates vs branch-level duplicates.
Earlier versions didn't backtrack properly due to missing pop()"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        s=[]
        nums.sort()
        def backtrack(index,path):
            s.append(path[:])
            for i in range(index,len(nums)):
                if nums[i]==nums[i-1] and i>index:
                    continue
                path.append(nums[i])
                backtrack(i+1,path)
                path.pop()
        backtrack(0,[])
        return s