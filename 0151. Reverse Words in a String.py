class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
        
OR:

class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        r = len(s)-1
        while True:
            while s[r] == ' ':
                r -= 1
            if r < 0:
                break
            l = r
            while l >= 0 and s[l] != ' ':
                l -= 1
            res.append(s[l+1:r+1])
            r = l
        return ' '.join(res)