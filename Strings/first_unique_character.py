class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for x in range(len(s)):
            count[s[x]] = count.get(s[x], 0) + 1
        for x,char in enumerate(s):
            if count[s[x]] == 1:
                return x
        return -1
