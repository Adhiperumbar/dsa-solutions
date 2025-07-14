"""
Leetcode 49: Group Anagrams
🗓️ Solved on: July 14, 2025

🧠 Problem:
Group together all the words in a list that are anagrams of each other.

🔍 Thought Process:
My first instinct was to use a dictionary and group words based on something common. 
Since anagrams have the same letters, I figured sorting each word would help. 
That sorted version could act as the key.

💡 What went wrong:
- I used `.sort()` on a string (which doesn’t work — it’s for lists only)
- I accidentally named my variable `str`, which clashed with Python’s built-in `str` type
- At one point, I tried comparing only one value instead of checking the entire dictionary

💪 What worked:
- Using `sorted(word)` followed by `''.join()` gave me a consistent key
- The dictionary grouped words perfectly under those keys
- Final return was just `list(anagram_map.values())`

📘 What I learned:
- Don’t blindly use `.sort()` — know when to use `sorted()`
- Be careful naming variables (never overwrite built-in types)
- Anagram problems often boil down to “how can I represent this word in a way that makes its letter pattern obvious?”

📌 Next Challenge:
Try solving the same problem using character frequency (like `Counter`) instead of sorting.

— Me, learning one mistake at a time
"""

from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anamap = {}
        for word in strs:
            key = ''.join(sorted(word))
            if key not in anamap:
                anamap[key] = []
            anamap[key].append(word)
        return list(anamap.values())
