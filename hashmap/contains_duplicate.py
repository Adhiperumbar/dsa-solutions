"""# 🚀 Problem: Contains Duplicate
# ✅ Date: 14-07-2025
# 💡 Category: Hashmap / Set
# 🎯 Difficulty: Easy
# 🧠 My Approach:
#   1. Tried using a nested loop to compare each number with others.
#      - It worked but got TLE on large inputs (O(n²) time complexity).
#   2. Switched to using a set to track seen elements.
#      - Initially made mistakes with `return` placement and `.add()` usage.
#      - Fixed it and learned how sets help avoid duplicates.
#   3. Understood the len(set) vs len(list) trick, but that wasn’t my original method.
# 📈 Time Complexity: O(n)
# 📦 Space Complexity: O(n)"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
