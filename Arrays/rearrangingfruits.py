"""📅 Date: August 2, 2025
🧠 Problem: LeetCode 2561 — https://leetcode.com/problems/rearranging-fruits/
🔧 Topic: Hash Maps (Counter), Sorting, Greedy, Minimum Cost
📚 Key Concepts Learned:
Using collections.Counter to track frequency of elements.
Comparing counters to check if two lists are already equal.
Using .extend() to add multiple elements to a list.
Why min(basket1 + basket2) is used for the 2× trick.
How surplus mismatched fruits are determined and balanced.
Greedy strategy to minimize cost using sorting and the min() function.
🚀 Approach Taken:
Counted fruit frequencies in both baskets using Counter.
Checked if baskets were already equal — returned 0 if so.
Built a surplus list by comparing actual vs ideal count (total // 2) for each fruit.
If any fruit had an odd total frequency → returned -1 (impossible case).
Sorted surplus to prioritize cheapest swaps first.
Found minfruit (cheapest fruit in both baskets).
Calculated cost for each required swap:
Direct swap: min(fruit)
Indirect swap via cheapest fruit: 2 * minfruit
Returned the total cost.
✅ What I Got Right:
Proper use of Counter for counting and comparison.
Correct logic to determine surplus fruits.
Efficient cost calculation using a greedy approach.
⚠️ What I Learned / Fixed:
Fixed the mistake of writing min(surplus, 2 * minfruit) instead of min(surplus[i], 2 * minfruit).
Understood difference between .extend() and .append().
Understood why min(basket1 + basket2) is used (the “via cheapest fruit” swap trick).
🌟 Reflection:
This was a hard problem, but I was able to break it down with help. I now feel much more confident about using Counter, list manipulation, and greedy logic for minimizing cost. Next time I’ll pay closer attention to data types passed into functions like min()."""

from collections import Counter
from typing import List
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        c1 = Counter(basket1)
        c2 = Counter(basket2)

        if c1 == c2:
            return 0

        surplus = []
        tc = c1 + c2

        for fruit in tc:
            total = c1[fruit] + c2[fruit]
            if total % 2 != 0:
                return -1

            diff = c1[fruit] - (total // 2)
            if diff > 0:
                surplus.extend([fruit] * diff)
            elif diff < 0:
                surplus.extend([fruit] * (-diff))

        surplus.sort()
        minfruit = min(basket1 + basket2)
        cost = 0

        for i in range(len(surplus) // 2):
            cost += min(surplus[i], 2 * minfruit)

        return cost