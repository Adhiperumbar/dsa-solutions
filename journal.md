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

# 🗓 Date: 15 July 2025
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

:
# 🗓 Date: 15 July 2025
✅ Problem: Isomorphic Strings
Category: Hashmap / Character Mapping

Difficulty: Easy

Approaches Tried:
❌ Tried using Counter and comparing sorted frequency values — failed because it ignored character positions.
✅ Then used two hashmaps: mapst to map s → t, and mapts to map t → s.
✅ Checked that the mapping is consistent at every index in both directions.

What I Learned:
Frequency-based comparison doesn’t work when position matters.
For "isomorphic" problems, a bijective (one-to-one and onto) mapping is required.
Need to track both s → t and t → s mappings to avoid false positives.
Clean if-else logic and proper indentation make or break these checks.

# 🗓 Date: 16 July 2025

Difficulty: Medium
📌 Problem: 3Sum
🧠 Approach: Brute-force using three nested loops
🕒 Time Complexity: O(n^3)
📦 Space Complexity: O(1) (excluding output)
📝 Notes:
- Sort the triplet before appending to avoid duplicate combinations
- Use 'not in result' check to ensure uniqueness

# 🗓 Date: 17 July 2025
✅ Problem Solved: Two Sum II – Input Array Is Sorted
Platform: LeetCode
Category: Two Pointers
Approach:
Used two pointers starting from both ends of the sorted array.
If the sum is greater than the target, move the right pointer left.
If the sum is less than the target, move the left pointer right.
If the sum matches the target, return the indices (1-based).
Time Complexity: O(n)
Space Complexity: O(1)

# 🗓 Date: 17 July 2025
✅ Problem Solved: Search Insert Position
Platform: LeetCode
Category: Binary Search
Approach:
Used binary search to efficiently locate the target index.
If the target is found, return the index.
If not found, return the index where it would be inserted to maintain the sorted order.
Time Complexity: O(log n)
Space Complexity: O(1)

# 🗓 Date: 17 July 2025

🧩 Problem 167: Two Sum II - Input Array Is Sorted (LeetCode)
🔗 Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
🚀 Approach: Two-Pointer Technique
⏱ Time Complexity: O(n)
🧠 Space Complexity: O(1)
🧠 Thought Process:
Since the array is sorted, I used two pointers: one at the start, one at the end.
If the sum is less than target, move left pointer.
If the sum is more than target, move right pointer.
If sum equals target, return indices (1-based).
🐞 Mistake I initially made:
I forgot that indices are **1-based** (not 0-based) as per the problem statement.
So I had to return [left + 1, right + 1].
# ✅ What I learned:
 Always read the problem constraints carefully (1-based indexing!).
Two-pointer strategy is very efficient for sorted arrays.

# 🗓 Date: 18 July 2025
✅ Problem: Minimum Size Subarray Sum
🔗 LeetCode: https://leetcode.com/problems/minimum-size-subarray-sum/
🗓️ Date Solved: 18-07-2025
🧠 Approach: Sliding Window
📝 Notes: I used a variable start to track the start of the sliding window. For each end, I add the value to sum. If sum >= target, I try to shrink the window from the left. Track the minimum window length. Return 0 if no valid subarray found.

# 🗓 Date: 19 July 2025
✅ Problem: Palindrome Linked List
🔗 LeetCode: https://leetcode.com/problems/palindrome-linked-list/
🗓️ Date Solved: 19-07-2025
🧠 Approach: Two Pointers + Reverse Second Half
📝 Notes:
Used slow and fast pointers to reach the middle of the linked list.
Reversed the second half of the list in-place.
Compared the first half and the reversed second half node-by-node.
If any mismatch is found, return False; otherwise, it's a palindrome.
No extra space used — O(n) time and O(1) space.

✅ Problem: Reverse Linked List
🔗 LeetCode: https://leetcode.com/problems/reverse-linked-list/
🗓️ Date Solved: 19-07-2025
🧠 Approach: Iterative Reversal
📝 Notes:
Used two pointers prev and cur to reverse the list in-place.
At each step, saved the next node and redirected cur.next to prev.
Updated pointers until reaching the end of the list.
Returned prev, which becomes the new head of the reversed list.
Time Complexity: O(n)
Space Complexity: O(1)

✅ Problem: Delete Node in a Linked List  
🔗 LeetCode: https://leetcode.com/problems/delete-node-in-a-linked-list/  
📅 Date Solved: 19-07-2025  
🧠 Approach: In-Place Node Overwrite  
📝 Notes:
- The node to be deleted is **not the tail**, and we are **not given head**.
- So instead of traditional deletion, I:
  - Copied the next node’s value into the current node.
  - Then bypassed the next node using `node.next = node.next.next`.
- This effectively "deletes" the given node by overwriting it.

> ✨ More to come as I keep solving and learning every day!
