# 📓 Leetcode DSA Progress Journal

This journal tracks my personal DSA learning journey using Python. Each entry reflects the problem I solved, my approach, what I learned, and personal reflections.  
I'm solving these to improve my logical thinking, consistency, and interview readiness.

---

## 📅 July 9, 2025

### ✅ Problem: Valid Anagram
- **Category:** String
- **Difficulty:** Easy
- **Approach:** Solved using both `Counter()` and `[0]*26` frequency array.
- **What I Learned:**
  - The use of `ord()` to map characters to indices.
  - When to use hashmaps vs arrays for performance.
- **Reflections:** I didn’t know about `ord()` initially and was confused, but breaking it down helped me internalize how ASCII works.

---

### ✅ Problem: First Unique Character in a String
- **Category:** String
- **Difficulty:** Easy
- **Approach:** Used dictionary to count characters, then checked first index with count = 1.
- **What I Learned:**
  - Difference between `count[char]` and `s.count(char)`.
  - Loop structure to avoid early returns.
- **Reflections:** Debugging this one helped me understand key-value access and order of operations. It was painful but worth it.

---

### ✅ Problem: Reverse Words in a String
- **Category:** String
- **Difficulty:** Medium
- **Approach:** Split string by whitespace, reversed list, joined with spaces.
- **What I Learned:**
  - `.split()` and `' '.join()` combo.
  - String immutability in Python.
- **Reflections:** I struggled with white space at first, but solved it. It felt awesome to crack string manipulation from scratch.

---

## 📅 July 10, 2025

### ✅ Problem: Two Sum
- **Category:** Array
- **Difficulty:** Easy
- **Approach:** Used dictionary to store target difference and check for complement.
- **What I Learned:**
  - Hashmap-based search for O(n) time.
  - Index tracking in arrays.
- **Reflections:** Felt like a solid logic boost. One of the first times I understood why brute force was slow.

---

### ✅ Problem: Best Time to Buy and Sell Stock
- **Category:** Array
- **Difficulty:** Easy
- **Approach:** Tracked minimum value and updated max profit on the fly.
- **What I Learned:**
  - Difference between current price and lowest so far.
  - How to simulate greedily over time series.
- **Reflections:** Loved the sliding window concept hidden inside. Visualization helped a lot.

---

### ✅ Problem: Median of Two Sorted Arrays (Brute Force)
- **Category:** Array
- **Difficulty:** Hard
- **Approach:** Merged both arrays, then picked the median directly.
- **What I Learned:**
  - Why brute force isn't scalable.
  - Median logic for even/odd lengths.
- **Reflections:** I know I need to improve this to binary search approach later. For now, I’m glad I got it working.

---

## 📅 July 14, 2025

### ✅ Problem: Group Anagrams
- **Category:** Hashmap
- **Difficulty:** Medium
- **Approach:** Used sorted version of strings as keys to group anagrams.
- **What I Learned:**
  - How to use `''.join(sorted(str))` as dictionary keys.
  - Grouping logic using `defaultdict`.
- **Reflections:** Felt smart solving this. Renaming folders for better structure also helped me feel organized.

---

### ✅ Problem: Valid Parentheses
- **Category:** Stack
- **Difficulty:** Easy
- **Approach:** Used a stack and a mapping dictionary to track brackets.
- **What I Learned:**
  - Stack basics (push on opening, pop on closing).
  - `return not stack` trick to ensure balance.
- **Reflections:** I blanked out initially and felt dumb, but once I pieced the logic together step by step, I felt unstoppable.

---

> ✨ More to come as I keep solving and learning every day!
