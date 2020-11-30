class Solution:
    def firstUniqChar(self, s: str) -> int:
        l = s
        t = [0 for i in range(26)]
        k = ord('a')
        ans = -1
        for i in range(len(l)-1,-1,-1):
            t[ord(l[i])-k] += 1
        for i in range(len(l)):
            if t[ord(l[i])-k] == 1:
                return i
        return -1