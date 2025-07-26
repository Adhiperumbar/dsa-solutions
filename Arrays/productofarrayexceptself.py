"""✅ Problem: Product of Array Except Self  
🔗 LeetCode: https://leetcode.com/problems/product-of-array-except-self/  
🗓️ Date Solved: 26-07-2025  
🧠 Approach: Prefix and Suffix Product Arrays (Optimized)  
📝 Notes:  
- **Goal:** Return an array where each element at index `i` is the product of all elements in the array except `nums[i]`.  
- **Constraints:** Division is not allowed, and the solution must be O(n) time.  
- Created a result array `res` initialized with 1s.  
- First pass (left to right): stored prefix product up to index `i`.  
- Second pass (right to left): multiplied the suffix product from the end.  
- Avoided extra space by storing prefix directly in `res` and using a single variable for suffix.  
- ✅ Time: O(n), ✅ Space: O(1) (excluding the output array).  
- A clean, efficient approach using two simple passes!
"""
