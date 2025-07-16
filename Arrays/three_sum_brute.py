"""
📌 Problem: 3Sum
🔗 Link: https://leetcode.com/problems/3sum/
🧠 Approach: Brute-force using three nested loops
🕒 Time Complexity: O(n^3)
📦 Space Complexity: O(1) (excluding output)
📝 Notes:
- Sort the triplet before appending to avoid duplicate combinations
- Use 'not in result' check to ensure uniqueness
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        count = sorted([nums[i], nums[j], nums[k]])
                        if count not in r:
                            r.append(count)
        return r
