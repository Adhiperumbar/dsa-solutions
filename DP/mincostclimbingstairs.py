"""
Date: 06-09-2025
Problem: Min Cost Climbing Stairs (LeetCode 746)
Problem Statement:
You are given an integer array cost where cost[i] is the cost of the i-th step. Once you pay the cost, you can climb either one or two steps. Find the minimum cost to reach the top of the floor.
Approach:
Handle base cases:
If len(cost) == 0, return 0.
If len(cost) == 1, return cost[0].
Use Dynamic Programming.
dp[i] = minimum cost to reach step i.
Initialize:
dp[0] = cost[0]
dp[1] = cost[1]
Recurrence:
dp[i] = cost[i] + min(dp[i-1], dp[i-2])
Final Answer:
To reach the top, you can come from either the last step or the second last step.
Return min(dp[n-1], dp[n-2]).
Key Concepts Used:
Dynamic Programming (Bottom-Up)
Recurrence Relation
Base Case Handling
Time Complexity: O(n) – iterate once through cost
Space Complexity: O(n) – used dp array
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if len(cost)==0:
            return 0
        elif len(cost)==1:
            return cost[0]
        dp=[0]*(len(cost))
        dp[0]=cost[0]
        dp[1]=cost[1]
        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        return min(dp[len(cost)-1],dp[len(cost)-2])