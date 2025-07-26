"""
💡 How I Solved It
First Try: Tried checking special cases with corner elements and manually modifying indices. Got messy and buggy.
Second Try: Tried using for i in range(1, len-1) loop, handled start and end separately. Still felt verbose.
Final Try (Best):
For each index i, check if current spot is 0.
If yes, check if left neighbor is 0 or i==0.
Check if right neighbor is 0 or i==len-1.
If both are empty, plant flower and increment count c.
Short-circuit return if c >= n early.
Much cleaner and greedy.
🧠 What I Learned
Greedy logic can solve this without backtracking.
Don’t overcomplicate with too many conditionals.
Edge handling is critical when working with arrays.
🕒 Time & Space Complexity
Time: O(n)
Space: O(1)"""
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                empty_left = (i == 0) or (flowerbed[i - 1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)
                if empty_left and empty_right:
                    flowerbed[i] = 1
                    c += 1
        return c >= n
