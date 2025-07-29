"""✅ Problem: Find the Difference of Two Arrays
🔗 LeetCode: https://leetcode.com/problems/find-the-difference-of-two-arrays/
🗓️ Date Solved: 29-07-2025
🧠 Approach: Set Difference using HashMap (Python set)
📝 Notes:
Goal: Return a list of two lists:
One containing elements only in nums1 but not in nums2
One containing elements only in nums2 but not in nums1
Used Python sets to remove duplicates and perform efficient difference operations.
Converted both arrays to sets to ensure uniqueness.
Used set difference (set1 - set2) to get unique elements.
Converted the result back to lists as required by the problem.
✅ Time: O(n + m), ✅ Space: O(n + m), where n and m are the lengths of the input arrays.
Simple and optimal approach leveraging Python set operations."""
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n=set(nums1)
        p=set(nums2)
        return [list(n-p),list(p-n)]