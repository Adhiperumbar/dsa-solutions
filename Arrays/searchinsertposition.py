"""# Date: 17 July 2025
# Problem: Search Insert Position (LeetCode)
# Approach: Binary Search
# Time Complexity: O(log n), Space Complexity: O(1)

# 🧠 Thought Process:
# - I used binary search because the array is sorted.
# - I initialized two pointers: left and right.
# - If the target is found, return the index.
# - If not found, return the position where it should be inserted (which is 'left' after loop).

# 🐞 Mistake I initially made:
# - I was returning `mid` when the target wasn't found, which gave wrong insert position.
# - Fixed it by returning `left` instead — because `left` ends up at the right insert spot.

# ✅ What I learned:
# - In binary search, when the target is not found, `left` will point to the correct insert index.
# - Always trace through an example to verify what your pointers are doing."""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                right=mid-1
            else:
                left=mid+1
        return mid