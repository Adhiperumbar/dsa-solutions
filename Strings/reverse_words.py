# Problem: Reverse Words in a String (LeetCode 151)
# Solved on: 09-07-2025
# Approach: Used split and reversed join
# Notes: Python string functions made this clean. Learned that strip and split handle spaces well.
# Plan: Try solving it without using built-in `split` or `join` to practice manual parsing.

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        rev_words=words[::-1]
        op=' '.join(rev_words)
        return op