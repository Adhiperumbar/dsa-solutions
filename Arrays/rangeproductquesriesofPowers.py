"""✅ Problem: Range Product Queries of Powers
🔗 LeetCode: https://leetcode.com/problems/range-product-queries-of-powers/
🗓️ Date Solved: 11-08-2025
🧠 Approach: Bit Manipulation + Prefix Sum
📝 Notes:
1. First, break down `n` into the minimal powers of 2 that sum to it.
   - This is equivalent to finding the positions of set bits (1s) in `n`'s binary form.
   - Each set bit at position `k` represents the power `2^k`.
   - Example: n = 15 (binary 1111) → exponents = [0, 1, 2, 3] → powers = [1, 2, 4, 8].

2. Instead of multiplying powers directly for each query:
   - We store only the **exponents** of 2 (k values).
   - The product of any range in powers = 2^(sum_of_exponents_in_that_range).

3. Build a **prefix sum array** of exponents to answer range sum queries in O(1).
   - prefix[i] stores sum of exponents from the start up to (i-1) index in exponents array.

4. For each query [l, r]:
   - Find sum of exponents: exp_sum = prefix[r+1] - prefix[l]
   - Result = pow(2, exp_sum, MOD)  (modular exponentiation to avoid large numbers).

5. Complexity:
   - Time: O(log n + q) where q = number of queries (log n from bit scanning).
   - Space: O(log n) for storing exponents and prefix sum.
   - No unnecessary recomputation, efficient even for large n.

6. Common pitfalls avoided:
   - Using `10^9 + 7` (XOR) instead of `10**9 + 7`.
   - Accidentally adding the whole list instead of a single exponent when building prefix sums.
"""
class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        exp = []
        bitpos = 0
        
        # Step 1: Get exponents from binary representation of n
        while n > 0:
            if n & 1:
                exp.append(bitpos)
            bitpos += 1
            n >>= 1
        
        # Step 2: Prefix sum of exponents
        pref = [0]
        for ex in exp:
            pref.append(pref[-1] + ex)
        
        # Step 3: Answer queries
        ans = []
        for l, r in queries:
            expsum = pref[r+1] - pref[l]
            ans.append(pow(2, expsum, MOD))
        
        return ans
