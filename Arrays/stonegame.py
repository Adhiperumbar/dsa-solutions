"""
Date: 04-09-2025
Problem: Stone Game (LeetCode 877)
Problem Statement:
Alice and Bob take turns picking stones from piles of stones arranged in a row. Each pile has a certain number of stones. Alice starts first. Given an array piles, return True if Alice can win, otherwise return False.
Approach (Your Code’s Version):
Initialize two sums → even for even-valued piles and odd for odd-valued piles.
Traverse through the piles:
If the pile value is even, add it to even.
Otherwise, add it to odd.
Compare the total sums:
Assign the larger sum to Alice and the smaller sum to Bob.
If Alice’s total > Bob’s total, return True, else return False.
Key Concepts Used:
Array traversal
Summation of subsets
Simple greedy check
Time Complexity: O(n) (where n = number of piles)
Space Complexity: O(1)
Observation / Note:
The classic Stone Game solution uses dynamic programming or mathematical reasoning (Alice always wins when n is even).
This approach checks based on even vs odd sums, which is a simplified greedy idea.
Status: ✅ Attempted with a working greedy approach.
"""
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        even = odd = 0
        for i in range(len(piles)):
            if piles[i] % 2 == 0:
                even += piles[i]
            else:
                odd += piles[i]
        if even > odd:
            alice, bob = even, odd
        else:
            alice, bob = odd, even
        return alice > bob