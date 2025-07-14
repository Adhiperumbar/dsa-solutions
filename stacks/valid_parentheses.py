"""
Leetcode 20: Valid Parentheses
🗓️ Solved on: July 14, 2025

🧠 Problem:
Check if a string containing only parentheses — (), {}, [] — is valid:
- Must be properly closed
- Must be properly nested

🔍 My Approach:
- Used a stack to track opening brackets
- Used a dictionary to match open-close pairs
- Pushed opening brackets
- For each closing bracket, popped from stack and matched with dictionary
- If mismatch or leftover brackets, return False

❗ Mistakes I caught:
- Tried to pop from an empty stack → added check before popping
- Forgot to return False when stack isn't empty at the end — fixed with `return not stack`

✅ What I learned:
- How stacks help in matching patterns like parentheses
- That popping without checking is risky 😅
- Returning `not stack` is a clean way to check balance

📌 Next up:
Try variations like:
- Removing invalid parentheses
- Longest valid substring
"""

class Solution:
    def isValid(self, s: str) -> bool:
        match={
            '[':']',
            '(':')',
            '{':'}'
        }
        if len(s)==1:
            return False
        stack = []
        for st in s:
            if st in match:
                stack.append(st)
            elif st in match.values():
                if not stack:
                    return False
                top=stack.pop()
                if match[top]!=st:
                    return False
        return not stack
            
