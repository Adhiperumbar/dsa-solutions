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

# 🗓 Date: 20 July 2025

✅ Problem: Remove Nth Node From End of List  
🔗 LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/  
📅 Date Solved: 20-07-2025  
🧠 Approach: Two-Pass Traversal  
📝 Notes:
- First, I traversed the list once to count the total number of nodes (`count`).
- Then I calculated the position from the start: `count - n`.
- If the node to be removed is the head, return `head.next`.
- Otherwise, traversed again to the node just before the one to be deleted.
- Skipped the `nth` node using: `cur.next = cur.next.next`.

# 🗓 Date: 21 July 2025

✅ Problem: Longest Substring Without Repeating Characters  
🔗 LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/  
📅 Date Solved: 21-07-2025  
🧠 Approach: Sliding Window with HashSet  
📝 Notes:
- Used a `set` to store unique characters in the current window.
- Used two pointers (`left` and `right`) to manage the window.
- If a duplicate character is found at `s[right]`, move the `left` pointer and remove characters from the set until it's unique again.
- After each iteration, update `maxlen` with the size of the current valid window.
- Time Complexity: O(n), Space Complexity: O(n)

✅ Problem: Subsets
🔗 LeetCode Link
🗓️ Date Solved: 21-07-2025
🧠 Approach: Backtracking (Recursive)
📁 Category: Recursion / Subsets / Backtracking
⚙️ Time Complexity: O(2^n)
🧮 Space Complexity: O(n) (path size during recursion)
💡 What I Learned:
Used backtracking to generate all possible subsets.
At each index, chose to either include or exclude an element.
Used path[:] to store a copy of current path, not reference (to avoid mutation issues).
Added subsets to the result list s at every recursive level.
Used path.pop() to backtrack after recursive call.

✅ Problem: Subsets II
🔗 LeetCode Link
🗓️ Date Solved: 21-07-2025
🧠 Approach: Backtracking with Duplicate Handling
📁 Category: Recursion / Backtracking / Subsets
⚙️ Time Complexity: O(2^n)
🧮 Space Complexity: O(n) (depth of recursive stack)
💡 What I Learned:
Used backtracking to generate all possible subsets even with duplicates.
Sorted the array to group duplicates together, which helped in skipping repeated branches.
The line if nums[i] == nums[i - 1] and i > index: ensures we skip duplicate elements only if they are not the first element at that level.
Added path[:] to result for a copy of current state.
Practiced how pruning the recursion tree reduces duplicate combinations.


# 🗓 Date: 22 July 2025

✅ Problem: Subset XOR Sum
🔗 LeetCode Link
🗓️ Date Solved: 22-07-2025
🧠 Approach: Backtracking
📁 Category: Recursion / Bit Manipulation / Subsets
⚙️ Time Complexity: O(2^n) — where n is the number of elements in nums
🧮 Space Complexity: O(n) — recursive stack depth
💡 What I Learned:
Used backtracking to explore all possible subsets.
At each step, made a choice to include or exclude the current element using XOR.
Maintained a total variable to accumulate the XOR values of all subsets.
Used nonlocal to modify the outer total variable from inside the nested function.

# 🗓 Date: 23 July 2025

✅ Problem: Permutations
🔗 LeetCode Link
🗓️ Date Solved: 23-07-2025
🧠 Approach: Backtracking
📁 Category: Backtracking / Recursion
⚙️ Time Complexity: O(n * n!)
🧮 Space Complexity: O(n) for the recursive call stack
💡 What I Learned:
Used a backtracking approach to generate all permutations.
Created a helper function backtrack(path) where path stores the current permutation.
Used if len(path) == len(nums) to check for completion of one permutation.
Appended a copy of path using path[:] to avoid reference issues.

# 🗓 Date: 24 July 2025
Problem: Kids With the Greatest Number of Candies
🔗 LeetCode: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
🗓️ Date Solved: 24-07-2025
🧠 Approach: Simple Iteration + Max
Time Complexity: O(n)
Space Complexity: O(n)
📝 Notes:
First found the current maximum candies any child has using max().
Then looped through each child's candy count and checked whether giving them extra candies would make them ≥ max.
Appended True or False accordingly to the result list.

✅ Problem: Greatest Common Divisor of Strings
🔗 LeetCode: https://leetcode.com/problems/greatest-common-divisor-of-strings/
🗓️ Date Solved: 24-07-2025
🧠 Approach: String Concatenation Check + Euclidean Algorithm
📝 Notes:
First, checked if str1 + str2 == str2 + str1. If not, there’s no common base string, so returned "".
If the check passed, used the Euclidean algorithm to find the GCD of the lengths of both strings.
Returned the substring of str1 from 0 to gcd(length1, length2) as the answer.

✅ Problem: Merge Strings Alternately
🔗 LeetCode: https://leetcode.com/problems/merge-strings-alternately/
🗓️ Date Solved: 24-07-2025
🧠 Approach: Index-Based Merging Using Lists
📝 Notes:
Converted both strings into lists to access characters by index.
Used a loop running up to the length of the longer word.
Added characters from each word if the index was within bounds.
Used ''.join(s) to convert the final list of characters into a merged string.
Also handled edge cases like empty input strings.

# 🗓 Date: 25 July 2025

✅ Problem: Remove Stars From a String
🔗 LeetCode: https://leetcode.com/problems/remove-stars-from-a-string
📅 Date Solved: 25-07-2025
🧠 Approach: Stack (using List)
📝 Notes:
I used a list t as a stack to simulate the removal of characters.
While traversing the string:
If the character is not "*", I added it to the stack.
If it is "*", I popped the last character from the stack.
After the loop, I joined the stack to form the final string.
This approach mimics a backspace-like behavior.
I understood how stacks can be useful in undo-type string manipulation.

✅ Problem: Delete the Middle Node of a Linked List
🔗 LeetCode: https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
🗓️ Date Solved: 25-07-2025
🧠 Approach: Two-pass Linked List Traversal
📝 Notes:
Handled edge cases where list is empty or has only one node.
First traversal to count total nodes (n).
Middle index calculated as n // 2.
Second traversal to reach node before middle.
Adjusted pointers to skip the middle node.
Returned modified linked list head.
Simple but requires two traversals.
Optimization possible using slow and fast pointers to achieve one pass.

# 🗓 Date: 26 July 2025

✅ Problem: Can Place Flowers
🔗 LeetCode: https://leetcode.com/problems/can-place-flowers/
🗓️ Date Solved: 26-07-2025
🧠 Approach: Greedy - Linear Scan with Local Conditions
📝 Notes:
Checked if a flower can be planted at index i by ensuring both neighbors are empty or nonexistent.
Edge cases like start (i == 0) and end (i == len - 1) handled using logical OR conditions.
If position valid, plant flower and increment count.
Early return if enough flowers are placed (c >= n).
Simple, clean, and efficient approach using O(1) space.
Avoided unnecessary backtracking or recursion.
Could optimize further by breaking early once condition is satisfied.

✅ Problem: Product of Array Except Self  
🔗 LeetCode: https://leetcode.com/problems/product-of-array-except-self/  
🗓️ Date Solved: 26-07-2025  
🧠 Approach: Prefix and Suffix Product Arrays (Optimized)  
📝 Notes:  
Goal:Return an array where each element at index `i` is the product of all elements in the array except `nums[i]`.  
Constraints: Division is not allowed, and the solution must be O(n) time.  
Created a result array `res` initialized with 1s.  
First pass (left to right): stored prefix product up to index `i`.  
Second pass (right to left): multiplied the suffix product from the end.  
Avoided extra space by storing prefix directly in `res` and using a single variable for suffix.  
✅ Time: O(n), ✅ Space: O(1) (excluding the output array).  
A clean, efficient approach using two simple passes!

# 🗓 Date: 28 July 2025

Problem: LeetCode 643 - Maximum Average Subarray I
Approach: Sliding Window (Fixed Size)
🔗 LeetCode: https://leetcode.com/problems/maximum-average-subarray-i/ 
✅ What I did:
Used a fixed-size sliding window of size `k`
Maintained a running sum for the current window
Updated max average by comparing with each new window sum
Key Learnings:
float('-inf') is helpful for max initialization
Sliding window avoids repeated summation => O(n) time, O(1) space
⚙️ Improvements:
Initially used a counter to track window size
Later simplified using index-based window sliding

✅ Problem: Maximum Number of Vowels in a Substring of Given Length
🔗 LeetCode: https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/
🗓️ Date Solved: 28-07-2025
🧠 Approach: Sliding Window (Fixed Size)
📝 Notes:
Goal: Find the maximum number of vowels in any substring of length k.
Used a fixed-size sliding window to maintain vowel count efficiently.
First, counted vowels in the initial window of size k.
Then, for each character moving into the window, updated the count by adding it (if vowel) and subtracting the character that slid out (if vowel).
Updated the max vowel count seen so far at each step.
This avoids recalculating vowels for each window and runs in linear time.
✅ Time: O(n), ✅ Space: O(1)
Clean and optimal use of sliding window for character counting problems!

# 🗓 Date: 29 July 2025

✅ Problem: Find the Difference of Two Arrays
🔗 LeetCode: https://leetcode.com/problems/find-the-difference-of-two-arrays/
🗓️ Date Solved: 29-07-2025
🧠 Approach: Set Difference using HashMap (Python set)

✅ Problem: Unique Number of Occurrences  
🔗 LeetCode: https://leetcode.com/problems/unique-number-of-occurrences/  
🗓️ Date Solved: 29-07-2025  
🧠 Approach: Frequency Map + Set  
📝 Notes:  
Goal: Check whether the number of times each element appears in the array is unique.  
Built a frequency dictionary `{element: count}` using a loop.  
Used `set(values)` to get distinct frequencies.  
If the number of unique frequencies equals the number of unique elements, return True.  
✅ Time: O(n), ✅ Space: O(n)  
A classic hashmap + set check for uniqueness!

# 🗓 Date: 30 July 2025

Problem: Max Consecutive Ones III
Link: [https://leetcode.com/problems/max-consecutive-ones-iii](https://leetcode.com/problems/max-consecutive-ones-iii)
Topic: Sliding Window
Difficulty: Medium
Date Solved: 30-07-25
✅ What I Learned
When asked for the longest subarray with at most `k` zeros flipped to `1`, use a sliding window.
Keep track of:
  `start` → left bound of the window
  `end` → right bound (expands over time)
  `count` → how many zeros are in the current window

Problem: Longest Subarray of 1's After Deleting One Element
Link: [https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element)
📅 Date Solved: 30-07-2025
🧠 Approach: Sliding Window
📄 Description:
Given a binary array nums, return the length of the longest subarray of 1's after deleting one element.
📝 Notes:
We’re allowed to delete one element, so the window can include at most one 0.
If there are more than 1 zero, shrink the window from the left.
We calculate the window size as end - start instead of end - start + 1 to simulate deletion of one element.
Efficient O(n) solution with constant space.

# 🗓 Date: 31 July 2025

Problem: Determine if Two Strings Are Close
Link: https://leetcode.com/problems/determine-if-two-strings-are-close
📅 Date Solved: 30-07-2025
🧠 Approach: Frequency Count + Set Comparison
📄 Description:
Two strings are close if you can attain one from the other using the following operations any number of times:
Swap any two characters.
Transform every occurrence of one character into another and vice versa.
📝 Notes:
First, check if both strings use exactly the same set of characters.
Then compare their frequency multisets (i.e., sorted counts of each character).
If both conditions are met, the strings are considered close.
This approach runs in O(n) time where n is the length of the strings.


# 🗓 Date: 01 August 2025 

"Problem: Maximum Median Sum
Link: https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/description/
📅 Date Solved: 01-08-2025
🧠 Approach: Greedy + Sorting
📄 Description:
Given an array of integers nums with length n = 3k, divide the array into k groups of 3 elements.
From each group, select the median (2nd largest element), and maximize the sum of these medians.
📝 Notes:
Sorted the array in ascending order.
To maximize the total median sum, chose every 2nd largest element from the last 3k elements.
Specifically, picked elements at positions: n-2, n-4, ..., down to n//3.
This strategy works because by choosing the top 3k numbers and carefully skipping one largest and one smallest per group, we can greedily pick the optimal medians.
✅ Time Complexity: O(n log n)
✅ Space Complexity: O(1)

Problem: Check Divisibility by Sum + Product of Digits
Link: https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/
📅 Date Solved: 30-07-2025
🧠 Approach: Digit Extraction + Arithmetic
📄 Description:
Given an integer n, check whether it is divisible by the sum of its digits plus the product of its digits.
📝 Notes:
Extracted each digit using modulo (% 10) and integer division (// 10).
Maintained two accumulators: digit_sum and digit_prod.
Added both to get total.
Final check: n % total == 0
Carefully avoided variable names like sum and prod to prevent overriding Python built-ins.
✅ Time Complexity: O(log₁₀n)
✅ Space Complexity: O(1)

# 🗓 Date: 02 August 2025 

🆔 Problem: 2561. Rearranging Fruits (Hard)
📅 Date Solved: 02-08-2025
🧠 Approach: Counter + Surplus Matching + Greedy Swapping
📄 Description:
You are given two fruit baskets (basket1 and basket2).
You can swap any fruit between the baskets at a cost of min(fruit1, fruit2).
The goal is to make the baskets identical (when sorted) using the minimum total cost, or return -1 if impossible.
📝 Notes:
Used collections.Counter to count fruit frequencies in both baskets.
Removed perfectly matching pairs (normalization step).
Checked if remaining mismatched counts were even (else return -1).
Constructed to_move1 and to_move2 lists containing surplus fruits from each basket.
Sorted to_move1 in ascending and to_move2 in descending order for greedy pairing.
For each pair, calculated minimum of:
direct swap cost,
swap via cheapest fruit: 2 * min(all fruits)
Summed all such minimum costs for final answer.
✅ Time Complexity:
O(n log n) due to sorting the surplus lists.
✅ Space Complexity:
O(n) for storing surplus fruit lists.
> ✨ More to come as I keep solving and learning every day!
