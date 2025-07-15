""" Problem Log: Top K Frequent Elements
🚀 Problem: Top K Frequent Elements
✅ Date: 15-07-2025
💡 Category: Hashmap / Heap
🎯 Difficulty: Medium
🧠 Approach:
First tried looping with Counter but misused int(freqmap) — learned that Counter returns a dictionary-like object.
Realized .most_common(k) gives top k elements as (element, freq) tuples.
Used list comprehension to return only the elements from the tuples.
Understood the mistake of checking if freqmap >= k — it's invalid comparison.
📈 Time Complexity: O(n log n)
📦 Space Complexity: O(n)"""
from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqmap = Counter(nums)
        return [item for item, count in freqmap.most_common(k)]
