"""✅ Problem: Remove Stars From a String
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
I understood how stacks can be useful in undo-type string manipulation."""
class Solution:
    def removeStars(self, s: str) -> str:
        t=[]
        for char in s:
            if char!="*":
                t.append(char)
            else:
                t.pop()
        return ''.join(t)
                