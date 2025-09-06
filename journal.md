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

Problem: Pascal’s Triangle
 Leetcode link : https://leetcode.com/problems/pascals-triangle
📅 Date Solved: 02-08-2025
🧠 Approach: Iterative Construction using Previous Row
📄 Description:
Generate the first numRows of Pascal’s Triangle, where each element is the sum of the two elements above it. The first and last elements of each row are always 1.
📝 Notes:
Initialized each row as a list of 1’s.
For inner elements, updated values by summing the two elements from the previous row.
Built the triangle row by row iteratively.
Time complexity: O(numRows^2)
Space complexity: O(numRows^2)

# 🗓 Date: 03 - 08 August 2025
Revision Week 

# 🗓 Date: 09 August 2025

Problem Name: Guess Number Higher or Lower 
📅 Date Solved: 09-08-2025
 Leetcode link : https://leetcode.com/problems/guess-number-higher-or-lower/
Concepts Used: Binary Search
Approach:
I used a binary search approach to efficiently guess the number between 1 and n.
Initially, set l = 1 and r = n.
While l <= r, find the midpoint mid = (l + r) // 2.
Use the provided guess() API to check:
If guess(mid) == 0, the correct number is found; return mid.
If guess(mid) == -1, the guessed number is too high; update r = mid - 1.
If guess(mid) == 1, the guessed number is too low; update l = mid + 1.
Reasoning:
Binary search minimizes the number of guesses by halving the search space each time, making it O(log n) in time complexity.
Time Complexity: O(log n)
Space Complexity: O(1)

# 🗓 Date: 10-08-2025
Problem Name: Reordered Power of 2
Leetcode Link: https://leetcode.com/problems/reordered-power-of-2
Difficulty: Medium
Problem Statement:
Given an integer n, return True if we can reorder the digits of n to form a power of two, and False otherwise. Reordering of digits includes not changing them at all.
Approach:
Convert n to a string and sort its digits to get the target arrangement.
Iterate over all powers of two from 2^0 to 2^30 (since 2^30 is the largest power of two within 10 digits).
Convert each power of two to a string, sort its digits, and compare with the target.
If any match is found, return True.
If no match is found after the loop, return False.
Time Complexity:
O(k log k) for sorting digits, where k is the number of digits in the number.
Since we loop 31 times, overall complexity is O(31 * k log k) → practically constant.
Space Complexity:
O(k) for storing the sorted digits.
What I Learned:
Powers of two have a very limited range for integers up to 10 digits, so brute-forcing all powers of two is efficient.
Using sorted(str(num)) is a quick way to compare permutations of digits.

# 🗓 Date: 11-08-2025
✅ Problem: Range Product Queries of Powers
🔗 LeetCode: https://leetcode.com/problems/range-product-queries-of-powers/
🗓️ Date Solved: 11-08-2025
🧠 Approach: Bit Manipulation + Prefix Sum
I learned how prefix sums can simplify problems involving cumulative counts. Instead of recalculating counts for each split, I used prefix arrays for 0s and suffix arrays for 1s, making the split score calculation efficient.
Time Complexity: O(n) – single pass to build prefix/suffix arrays + single pass to find max score.
Space Complexity: O(n) – storing prefix and suffix arrays.

# 🗓 Date: 12-08-2025

✅ Problem: Remove Duplicates from Sorted Linked List
🔗 LeetCode: 83. Remove Duplicates from Sorted List
🗓️ Date Solved: 12-08-2025
🧠 Approach: HashSet + Iteration
Used a visited set to store unique values while traversing the linked list.
Maintained two pointers:
cur → current node
prev → last unique node
If the current node’s value is already in visited, skipped it by updating prev.next.
Otherwise, added it to visited and moved prev forward.
💡 Key Points:
Works for both sorted and unsorted linked lists.
Uses O(n) extra space for the set.
Alternative: For sorted lists, you can solve it in-place with O(1) space by skipping duplicates directly.
⏱ Complexity:
Time: O(n) — traverses the list once.
Space: O(n) — extra space for the visited set.

# 🗓 Date: 13-08-2025

Problem: LeetCode #21 — Merge Two Sorted Lists
Approach: Iterative with Dummy Node
Date: 13-08-2025
Problem Understanding:
We are given two sorted linked lists (list1 and list2).
We must merge them into one sorted linked list in ascending order without creating new nodes (just rearranging links).
Key Idea:
Use a dummy node to simplify list handling — avoids special cases for the head.
Maintain a tail pointer that always points to the last node in the merged list.
Compare the current nodes of list1 and list2, attach the smaller one to tail, and move that list forward.
When one list is exhausted, attach the remainder of the other list.

✅ Problem: Power of Three
🔗 LeetCode: https://leetcode.com/problems/power-of-three
🗓️ Date Solved: 13-08-2025
🧠 Approach: Iterative Division + Backtracking
I learned that checking if a number is a power of three can be done by repeatedly dividing by 3 until reaching 1 (iterative) or by recursively multiplying by 3 starting from 1 (backtracking). Iterative division is more space-efficient, while backtracking is useful for practicing recursion patterns.
Time Complexity: O(log₃ n) – number reduces by a factor of 3 each step.
Space Complexity:
Iterative: O(1) – constant extra space.
Backtracking: O(log₃ n) – recursion stack space.

# 🗓 Date: 14-08-2025

✅ Problem: Largest 3-Same-Digit Number in String
🔗 LeetCode: https://leetcode.com/problems/largest-3-same-digit-number-in-string/
🗓️ Date Solved: 14-08-2025
🧠 Approach: Sliding Window (size = 3)
I used a fixed-size sliding window to check every triplet in the string. For each window, if all three digits were the same, I compared it with my current maximum. Since the input remains a string, direct lexicographic comparison worked. Learned the importance of avoiding unnecessary list() conversion in string problems — it broke comparisons earlier by turning slices into lists. Also, remembered not to shadow built-in functions like max.

# 🗓 Date: 15-08-2025

✅ Problem: Power of Four
🔗 LeetCode: https://leetcode.com/problems/power-of-four/
🗓️ Date Solved: 15-08-2025
🧠 Approach: Iterative Division
I checked if n is a positive number first. Then, I repeatedly divided n by 4 as long as it was divisible by 4. If the final result equals 1, then n is a power of four. This approach is simple, avoids floating-point issues, and has logarithmic complexity.

# 🗓 Date: 17-08-2025

✅ Problem: Maximum 69 Number
🔗 LeetCode: https://leetcode.com/problems/maximum-69-number/
🗓️ Date Solved: 17-08-2025
🧠 Approach: String Replacement
The problem asks to maximize a number made of digits 6 and 9 by changing at most one digit. The greedy choice is to change the first occurrence of 6 into 9, since that affects the highest place value. I solved it by converting the integer to a string, replacing the first '6' with '9', and converting it back to int. This is both concise and efficient.
Complexities:
⏱ Time Complexity: O(d) where d is the number of digits in num (string conversion + replace + int conversion).
📦 Space Complexity: O(d) for storing the string representation of num.


# 🗓 Date: 19-08-2025

Problem: Number of Zero-Filled Subarrays (LeetCode 2348)
Problem Link: https://leetcode.com/problems/number-of-zero-filled-subarrays
Date Solved: 19-08-2025
Approach: Counting Consecutive Zeros
Iterate through the array while tracking consecutive zeros (count).
When a non-zero appears, calculate subarrays from the streak:
subarrays=count×(count+1)
Reset count and continue.
At the end, add contribution of the last streak.
Complexity:
Time: O(n) (single pass)
Space: O(1) (only counters used)

# 🗓 Date: 20-08-2025

✅ Problem: Binary Tree Inorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal   
🗓️ Date Solved: 20-08-2025
🧠 Approach: Iterative Inorder Traversal using Stack
Used a stack to simulate the recursive behavior of inorder traversal.
Keep pushing nodes while going left, then pop, process value, and move right.
This avoids recursion and handles large trees efficiently.
📜 Key Steps:
Initialize stack = [] and cur = root.
Traverse left until cur is None, pushing nodes to stack.
Pop node from stack, add its value to res.
Move to right child and repeat until both stack and cur are empty.
⏱️ Complexity:
Time: O(n) (every node is pushed and popped once).
Space: O(n) (stack in worst case when tree is skewed).
💡 Learning:
Iterative inorder traversal is a great alternative to recursion.
Helped me understand how recursion works under the hood by mimicking the call stack manually.

# 🗓 Date: 21-08-2025

✅ Problem: 144. Binary Tree Preorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-preorder-traversal/
🗓️ Date Solved: 21-08-2025
🧠 Approach: Iterative Preorder Traversal using Stack
Preorder traversal follows Root → Left → Right order.
Used a stack to simulate recursion.
Start by pushing the root node into the stack.
At each step:
Pop the node, process it (res.append(node.val)),
Push the right child (if any), then the left child (if any) → ensures left is processed first.
⏱️ Time Complexity: O(n) – each node is visited once.
💾 Space Complexity: O(n) – in the worst case (skewed tree), the stack holds all nodes.
✅ Key Learning
Preorder traversal can be done iteratively by pushing nodes in reverse order (right before left) to maintain correct processing order. This avoids recursion and works efficiently for large trees.

✅ Problem: 145. Binary Tree Postorder Traversal
🔗 LeetCode: https://leetcode.com/problems/binary-tree-postorder-traversal/
🗓️ Date Solved: 22-08-2025
🧠 Approach: Iterative Postorder Traversal using Two Stacks
Postorder traversal follows Left → Right → Root order.
Used two stacks to simulate recursion and reverse the node processing order.
Start by pushing the root node into the first stack.
At each step:
Pop a node from the first stack and push its value to the second stack.
Push the left child (if any), then the right child (if any) into the first stack.
After processing all nodes, pop all values from the second stack to get the postorder sequence.
⏱️ Time Complexity: O(n) – each node is visited once.
💾 Space Complexity: O(n) – in the worst case, both stacks hold all nodes.
✅ Key Learning:
Postorder traversal can be implemented iteratively by reversing the processing order of a modified preorder traversal (Root → Right → Left) using two stacks. This method provides a clear and efficient way to perform postorder traversal without recursion.

# 🗓 Date: 26-08-2025

✅ Problem: House Robber
🔗 LeetCode Link: https://leetcode.com/problems/house-robber/ 
🗓️ Date Solved: 26-08-2025
🧠 Approach: Dynamic Programming (Optimized with Two Variables)
Maintained two variables:
rob1 → maximum amount robbed up to the previous house
rob2 → maximum amount robbed up to the house before the previous one
For each house value num:
Calculated new_rob = max(rob1, rob2 + num)
Updated rob2 = rob1 and rob1 = new_rob
Returned rob1 as the maximum amount that can be robbed.
💡 Key Points:
Optimized solution using O(1) space instead of a full DP array.
Simple and clean iteration, only updating two variables.
Works for any list of non-negative house values.
⏱ Complexity:
Time: O(n) — iterates through the list once.
Space: O(1) — only two extra variables used.

# 🗓 Date: 27-08-2025
# 🗓 Date: 27-08-2025

✅ Problem: House Robber II (Circular Houses)
🔗 LeetCode: https://leetcode.com/problems/house-robber-ii/
🗓️ Date Solved: 27-08-2025
🧠 Approach: Dynamic Programming + Two Variables
Since the houses are circular, the first and last house cannot both be robbed
Defined a helper function robb to solve the linear version (House Robber I) using two variables
rob1 → maximum up to previous house
rob2 → maximum up to house before previous
For each house value
new = max(rob1, rob2 + num)
Update rob2 = rob1, rob1 = new
Solved two cases separately:
Rob houses from first to second-last (nums[:-1])
Rob houses from second to last (nums[1:])
Returned the maximum of the two cases.
💡 Key Points:
Reduces the circular problem to two linear subproblems.
Optimized O(1) space by using only two variables.
Works for empty lists or single-house cases.
⏱ Complexity:
Time: O(n) — iterates through each sublist once.
Space: O(1) — only a few variables used, no extra data structures.

# 🗓 Date: 29-08-2025

✅ Problem: Difference Between Sum of Even and Odd Numbers
🗓️ Date Solved: 29-08-2025
🧠 Approach: Iteration + Simple Arithmetic
First input n → size of array, followed by n numbers.
Traversed through each number in the array.
Maintained two sums:
even_sum → sum of all even numbers
odd_sum → sum of all odd numbers
Final answer = abs(even_sum - odd_sum) (absolute difference).
💡 Key Points:
Straightforward iteration over array.
Used modulo % operator to check even/odd.
abs() ensures result is always non-negative.
⏱ Complexity:
Time: O(n) — traverses the array once.
Space: O(1) — only a few variables used.


# 🗓 Date: 30-08-2025

✅ Problem: Maximum Subarray
🔗 LeetCode: 53. Maximum Subarray
🗓️ Date Solved: 30-08-2025
🧠 Approach: Kadane’s Algorithm (Dynamic Programming)
Maintained two variables:
cs → current maximum subarray sum ending at current index
ms → overall maximum subarray sum found so far
For each element nums[i]:
cs = max(nums[i], cs + nums[i]) → either start new subarray or extend current one
ms = max(ms, cs) → update overall maximum
Returned ms as the maximum subarray sum.
💡 Key Points:
Efficient O(n) time solution using O(1) space.
Handles negative numbers and all-positive arrays.
Simple iteration with dynamic updating of sums.
⏱ Complexity:
Time: O(n) — single pass through the array.
Space: O(1) — only two variables used.

# 🗓 Date: 31-08-2025

✅Problem: Count and Say
🔗LeetCode: 38. Count and Say
🗓️Date Solved: 31-08-2025
🧠Approach: Iterative String Construction
Start with res="1".
For each iteration up to n: traverse res, count consecutive identical digits, build temp="<count><digit>", then update res=temp.
Return res after n iterations.
💡Key Points:
Nested loops count consecutive characters.
Builds next term iteratively without recursion.
Works for all n≥1.
⏱Complexity:
Time: O(2ⁿ)
Space: O(2ⁿ)

# 🗓 Date: 01-09-2025

Date: 01-09-2025
Problem: Add Binary
Problem Statement:
Given two binary strings a and b, return their sum as a binary string.
Approach:
Start from the last index of both strings (i for a, j for b).
Maintain a variable c for carry and a list res for storing result digits.
Loop while i >= 0 or j >= 0 or there is a carry.
Initialize t with the carry.
If i >= 0, add a[i] to t and move i left.
If j >= 0, add b[j] to t and move j left.
Append t % 2 (binary digit) to res.
Update c = t // 2.
Reverse the result list and join to form the final binary string.
Key Concepts Used:
Two pointer approach (right to left).
Carry handling in binary addition.
String manipulation and reversing.
Time Complexity: O(n) (where n = max(len(a), len(b)))
Space Complexity: O(n) (for the result list).

# 🗓 Date: 02-09-2025

Date: 02-09-2025
Explanation:
Convert binary strings a and b to integers.
Use bitwise operations to simulate binary addition:
carry = a & b → identifies positions where both bits are 1.
a = a ^ b → adds bits without considering carry.
b = carry << 1 → shifts carry left (since carry applies to the next higher bit).
Repeat until b becomes 0 (no more carry).
Convert final integer result back to binary string using bin(a)[2:].
Learning/Observation:
This approach avoids string reversal and manual digit-by-digit addition.
Works entirely with bitwise operators (&, ^, <<).
Mimics how hardware binary addition works.
More efficient than handling strings when numbers are large.

# 🗓 Date: 03-09-2025

Date: 03-09-2025
Problem: Find the Index of the First Occurrence in a String
Problem Statement:
Given two strings haystack and needle, return the index of the first occurrence of needle in haystack. If needle is not part of haystack, return -1.
Approach:
Loop from i = 0 to len(haystack) - len(needle).
For each index, take the substring haystack[i : i + len(needle)].
If the substring equals needle, return the index i.
If no match is found after the loop, return -1.
Key Concepts Used:
String slicing
Brute force substring search
Time Complexity: O((n - m + 1) * m), where n = len(haystack) and m = len(needle)
Space Complexity: O(1)

# 🗓 Date: 04-09-2025

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

# 🗓 Date: 05-09-2025

Date: 05-09-2025
Problem: Climbing Stairs (LeetCode 70)
Problem Statement:
You are climbing a staircase with n steps. You can take either 1 or 2 steps at a time. Return the number of distinct ways to reach the top.
Approach:
Handle base cases:
If n == 1, return 1.
If n == 2, return 2.
Use dynamic programming to store the number of ways to reach each step:
Initialize dp array of size n.
dp[0] = 1 → 1 way to reach step 1.
dp[1] = 2 → 2 ways to reach step 2.
For each step i from 2 to n-1:
dp[i] = dp[i-1] + dp[i-2] → ways to reach step i = sum of ways to reach previous two steps.
Return dp[n-1] as the total number of ways.
Key Concepts Used:
Dynamic Programming
Fibonacci sequence pattern
Time Complexity: O(n) – single pass to fill DP array
Space Complexity: O(n) – DP array of size n

Optimised solution:
Date: 05-09-2025
Problem: Climbing Stairs (LeetCode 70)
Problem Statement:
You are climbing a staircase with n steps. You can take either 1 or 2 steps at a time. Return the number of distinct ways to reach the top.
Approach (Optimized Space):
Handle base case: if n == 1, return 1.
Use two variables a and b to track the number of ways to reach the previous two steps:
a = 1 → ways to reach step 1
b = 2 → ways to reach step 2
For each step i from 2 to n-1:
Update a, b = b, a + b → shift previous values and calculate current ways.
Return b as the total number of ways to reach step n.
Key Concepts Used:
Dynamic Programming
Fibonacci sequence pattern
Space optimization using two variables
Time Complexity: O(n) – iterates through steps once
Space Complexity: O(1) – only two variables used

Date: 05-09-2025
Problem: Fibonacci Number (LeetCode 509)
Problem Statement:
Given n, return the nth Fibonacci number. The Fibonacci sequence is defined as:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) for n > 1
Approach (Dynamic Programming):
Handle base cases:
If n == 0, return 0
If n == 1, return 1
Initialize a DP array dp of size n+1.
dp[0] = 0
dp[1] = 1
For each i from 2 to n:
dp[i] = dp[i-1] + dp[i-2] → store the Fibonacci value at i.
Return dp[n] as the nth Fibonacci number.
Key Concepts Used:
Dynamic Programming
Bottom-up computation of Fibonacci numbers
Time Complexity: O(n) – single pass through the array
Space Complexity: O(n) – DP array of size

Optimised Solution:
Approach (Space-Optimized):
Handle base cases:
If n == 0, return 0
If n == 1, return 1
Use two variables a and b to store the previous two Fibonacci numbers:
a = 0 → F(0)
b = 1 → F(1)
For each i from 2 to n:
Update a, b = b, a + b → shift previous values and compute current Fibonacci number.
Return b as the nth Fibonacci number.
Key Concepts Used:
Dynamic Programming / Fibonacci sequence
Space optimization using two variables
Time Complexity: O(n) – iterate through 2 to n
Space Complexity: O(1) – only two variables used

# 🗓 Date: 06-09-2025

Date: 06-09-2025
Problem: Maximum Sum Circular Subarray (LeetCode 918)
Problem Statement:
Given a circular integer array nums, return the maximum possible sum of a non-empty subarray. The subarray may wrap around (i.e., connect the end of the array to the beginning).
Approach:
Use a modified version of Kadane’s Algorithm to track both maximum and minimum subarray sums.
currentmax, maxsum → track maximum subarray sum.
currentmin, minsum → track minimum subarray sum.
For each element:
Update currentmax = max(nums[i], currentmax + nums[i]).
Update maxsum = max(maxsum, currentmax).
Update currentmin = min(nums[i], currentmin + nums[i]).
Update minsum = min(minsum, currentmin).
Special Case:
If all numbers are negative, return maxsum (since sum(nums) - minsum would be zero).
Otherwise, return max(maxsum, sum(nums) - minsum) to cover both normal and circular subarrays.
Key Concepts Used:
Kadane’s Algorithm
Circular array handling
Edge case check (all negatives)
Time Complexity: O(n) – single traversal of the array
Space Complexity: O(1) – constant variables used

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

Date: 06-09-2025
Problem: Maximum Product Subarray (LeetCode 152)
Problem Statement:
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest product, and return that product.
Approach:
This is similar to Maximum Subarray Sum, but products behave differently due to negative numbers.
At each index i, track two values:
cmax: the maximum product ending at i.
cmin: the minimum product ending at i.
Reason: a negative number can flip min ↔ max.
If nums[i] is negative, swap cmax and cmin.
Update:
cmax = max(nums[i], cmax * nums[i])
cmin = min(nums[i], cmin * nums[i])
Track the result:
res = max(res, cmax)
Key Concepts Used:
Dynamic Programming (Kadane’s variant)
Handling negative numbers by maintaining both min & max
Greedy updating in one pass
Time Complexity: O(n) – iterate once through nums
Space Complexity: O(1) – constant extra space

> ✨ More to come as I keep solving and learning every day!
