"""# LeetCode Problem: Two Sum II - Input Array Is Sorted
# Approach: Two Pointers
# Time Complexity: O(n)
#Date:17/07/25
"""
from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        while l<r:
            cs=numbers[l]+numbers[r]
            if cs==target:
                return [l+1,r+1]
            elif cs>target:
                r-=1
            else:
                l+=1
        return [l+1,r+1]