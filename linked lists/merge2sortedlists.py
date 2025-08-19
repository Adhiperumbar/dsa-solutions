"""
Date: 13-08-2025
Problem: LeetCode #21 — Merge Two Sorted Lists
Approach: Iterative with Dummy Node
Problem Understanding:
We are given two sorted linked lists (list1 and list2).
We must merge them into one sorted linked list in ascending order without creating new nodes (just rearranging links).
Key Idea:
Use a dummy node to simplify list handling — avoids special cases for the head.
Maintain a tail pointer that always points to the last node in the merged list.
Compare the current nodes of list1 and list2, attach the smaller one to tail, and move that list forward.
When one list is exhausted, attach the remainder of the other list.
"""