# Problem: Best Time to Buy and Sell Stock (LeetCode 121)
# Solved on: 10-07-2025
# Approach: Single pass, tracking min price and max profit
# Notes: Understood the concept of maintaining a min-so-far and calculating profit as we go.
# Plan: Try writing variations (multiple transactions, cooldown) in future.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minp=prices[0]
        maxp=0
        for i in range(1,len(prices)):
            if prices[i]<minp:
                minp=prices[i]
            else :
                profit= prices[i]-minp
                if profit>maxp:
                    maxp=profit
        return maxp