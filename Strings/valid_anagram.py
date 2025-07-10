class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charlist=[0]*26
        for i in s:
            index=ord(i)-ord('a')
            charlist[index]+=1
        for i in t:
            index=ord(i)-ord('a')
            charlist[index]-=1
            return charlist!=[0]*26
            