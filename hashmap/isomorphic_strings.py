"""# 🗓️ 15-07-2025
#
# ✅ Problem: Isomorphic Strings
#
# 📂 Category: Hashmap / Character Mapping
# 🟢 Difficulty: Easy
#
# ✅ Approaches Tried:
#   1. ❌ Tried using Counter and comparing sorted frequency values — did not work because position-based mapping is required.
#   2. ✅ Used two dictionaries: `mapst` for s → t and `mapts` for t → s mapping.
#   3. ✅ Verified mapping is consistent at every index in both directions using for-loop.
#
# 📚 What I Learned:
#   - Frequency counts alone are not enough when character **positions** matter.
#   - A valid isomorphic string mapping requires a **one-to-one and onto** relationship.
#   - Need to track both directions (s → t and t → s) to avoid incorrect mappings.
#
# ⏱️ Time Complexity: O(n)
# 🗃️ Space Complexity: O(n)"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapst = {}
        mapts = {}

        for i in range(len(s)):
            char1 = s[i]
            char2 = t[i]

            if char1 in mapst:
                if mapst[char1] != char2:
                    return False
            else:
                mapst[char1] = char2

            if char2 in mapts:
                if mapts[char2] != char1:
                    return False
            else:
                mapts[char2] = char1

        return True
