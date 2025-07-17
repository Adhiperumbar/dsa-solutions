"""# 🗓 Date: 17 July 2025
# 🧩 Problem 167: Two Sum II - Input Array Is Sorted (LeetCode)
# 🔗 Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# 🚀 Approach: Two-Pointer Technique
# ⏱ Time Complexity: O(n)
# 🧠 Space Complexity: O(1)

# 🧠 Thought Process:
# - Since the array is sorted, I used two pointers: one at the start, one at the end.
# - If the sum is less than target, move left pointer.
# - If the sum is more than target, move right pointer.
# - If sum equals target, return indices (1-based).

# 🐞 Mistake I initially made:
# - I forgot that indices are **1-based** (not 0-based) as per the problem statement.
# - So I had to return [left + 1, right + 1].

# ✅ What I learned:
# - Always read the problem constraints carefully (1-based indexing!).
# - Two-pointer strategy is very efficient for sorted arrays."""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        mxar = 0
        while l < r:
            # Width is the distance between two lines
            w = r - l
            # Height is the shorter line (limiting factor)
            minh = min(height[l], height[r])
            ar = w * minh
            mxar = max(mxar, ar)
            
            # Move the pointer with the shorter line
            # because moving the longer one won't help
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1  # ← THIS was the mistake earlier
        return mxar