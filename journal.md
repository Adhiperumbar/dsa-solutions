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

## 🗓️ 14-07-2025

### ✅ Problem: Contains Duplicate

- **Category:** Hashmap / Set
- **Difficulty:** Easy
- **Approaches Tried:**
  1. ✅ Tried using nested loops — worked, but got TLE due to O(n²) complexity.
  2. ✅ Then tried using a set to track duplicates — learned that set lookup is O(1), so this gives O(n) time.
  3. ✅ Also implemented a set-based logic comparing `len(set(nums))` with `len(nums)` — concise and efficient.

- **What I Learned:**
  - Sets automatically ignore duplicates.
  - Always be careful with where `return` statements are placed.
  - Efficiency matters when input size is large.
  - Comparing lengths is a smart shortcut when checking for duplicates.

- **Final Approach Used:**  
  ```python
  class Solution:
      def containsDuplicate(self, nums: List[int]) -> bool:
          return len(set(nums)) != len(nums)

🗓️ 15-07-2025
✅ Problem: Top K Frequent Elements
Category: Hashmap / Heap
Difficulty: Medium
Approaches Tried:
❌ Initially tried looping over nums and using int(freqmap) >= k — realized this doesn't make sense because freqmap is a dictionary (Counter), not an integer.
✅ Learned about Counter(nums).most_common(k) — gives the top K frequent items as a list of (element, frequency) tuples.
✅ Used a list comprehension [item for item, count in freqmap.most_common(k)] to extract just the elements.
✅ Understood that sorting and extracting top K using frequency is cleaner and more efficient than manual looping.
What I Learned:
Counter is a subclass of dict from collections that simplifies frequency counting.
.most_common(k) directly returns the top K frequent items — very useful!
List comprehensions can be used to cleanly extract data from tuples.
Misusing type conversions (int(freqmap)) leads to logical errors.

> ✨ More to come as I keep solving and learning every day!
