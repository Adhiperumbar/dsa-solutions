"""Date: 09 August 2025
Problem Name: Guess Number Higher or Lower (LeetCode #374)
Concepts Used: Binary Search
Approach:
I used a binary search approach to efficiently guess the number between 1 and n.
Initially, set l = 1 and r = n.
While l <= r, find the midpoint mid = (l + r) // 2.
Use the provided guess() API to check:
If guess(mid) == 0, the correct number is found; return mid.
If guess(mid) == -1, the guessed number is too high; update r = mid - 1.
If guess(mid) == 1, the guessed number is too low; update l = mid + 1.
Reasoning:
Binary search minimizes the number of guesses by halving the search space each time, making it O(log n) in time complexity.
Time Complexity: O(log n)
Space Complexity: O(1)
"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=(l+r)//2
            res=guess(mid)
            if res==0:
                return mid
            if res==-1:
                r=mid-1
            else:
                l=mid+1
