"""🔹 Problem: Longest Subarray of 1's After Deleting One Element (LeetCode #1493)
📅 Date Solved: 30-07-2025
🧠 Approach: Sliding Window
📄 Description:
Given a binary array nums, return the length of the longest subarray of 1's after deleting one element.
📝 Notes:
We’re allowed to delete one element, so the window can include at most one 0.
If there are more than 1 zero, shrink the window from the left.
We calculate the window size as end - start instead of end - start + 1 to simulate deletion of one element.
Efficient O(n) solution with constant space."""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        c=0
        start=0
        mx=0
        for end in range(len(nums)):
            if nums[end]==0:
                c+=1
            while c>1:
                if nums[start]==0:
                    c-=1
                start+=1
            mx=max(mx,end-start)
        return mx