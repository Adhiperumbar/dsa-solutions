"""# Date Solved: 28/07
# Problem: LeetCode 643 - Maximum Average Subarray I
# Approach: Sliding Window (Fixed Size)
#
# ✅ What I did:
# - Used a fixed-size sliding window of size `k`
# - Maintained a running sum for the current window
# - Updated max average by comparing with each new window sum
#
# 💡 Key Learnings:
# - float('-inf') is helpful for max initialization
# - Sliding window avoids repeated summation => O(n) time, O(1) space
#
# ⚙️ Improvements:
# - Initially used a counter to track window size
# - Later simplified using index-based window sliding
#
# 🌟 Result:
# - Passed all test cases on LeetCode
# - Learned to trust my logic and optimize it step-by-step

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Initial sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, len(nums)):
            window_sum = window_sum - nums[i - k] + nums[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum / k
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        mx=float('-inf')
        start=0
        sum=0
        c=0
        for end in range(len(nums)):
            sum+=nums[end]
            c+=1
            if c==k:
                mx=max(mx,sum/k)
                sum-=nums[start]
                start+=1
                c-=1
        return mx