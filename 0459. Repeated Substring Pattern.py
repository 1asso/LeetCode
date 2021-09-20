KMP:

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        j = 0
        n = len(s)
        next = [0, 0]
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = next[j]
            if s[i] == s[j]:
                j += 1
            next.append(j)
        pat = next[-1]
        return pat and n % (n - pat) == 0
        

Fold & find:

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]