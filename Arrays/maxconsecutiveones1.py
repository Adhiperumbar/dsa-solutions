"""📘 Journal Entry
Problem: Max Consecutive Ones III
Link: [https://leetcode.com/problems/max-consecutive-ones-iii](https://leetcode.com/problems/max-consecutive-ones-iii)
Topic: Sliding Window
Difficulty: Medium
Date Solved: 30-07-25
✅ What I Learned
When asked for the longest subarray with at most `k` zeros flipped to `1`, use a sliding window.
Keep track of:
  `start` → left bound of the window
  `end` → right bound (expands over time)
  `count` → how many zeros are in the current window
Shrink the window when `count > k`.
🧠 Key Insight
"Track only how many zeros are in the window. Shrink window from the left until you satisfy the `k` flips again."
⚠️ Mistakes I Made
Initially tried modifying the input array (`nums[end] = 1`) — this is not needed and causes side effects.
Forgot to handle edge cases like when `end` starts from `0`, not `1`.
Didn’t place `mx = max(mx, end - start + 1)` inside the loop.
"""
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        count = 0 
        mx = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count += 1
            while count > k:
                if nums[start] == 0:
                    count -= 1
                start += 1
            mx = max(mx, end - start + 1)

        return mx