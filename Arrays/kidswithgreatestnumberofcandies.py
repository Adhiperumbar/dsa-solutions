""" Problem: Kids With the Greatest Number of Candies
🔗 LeetCode: https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
🗓️ Date Solved: 24-07-2025
🧠 Approach: Simple Iteration + Max
📝 Notes:
First found the current maximum candies any child has using max().
Then looped through each child's candy count and checked whether giving them extra candies would make them ≥ max.
Appended True or False accordingly to the result list."""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest=max(candies)
        s=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies >= greatest:
                s.append(True)
            else:
                s.append(False)
        return s