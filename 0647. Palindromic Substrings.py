DP:

class Solution:
    def countSubstrings(self, s: str) -> int:
        l = len(s)
        dp = [[False] * l for _ in range(l)] # dp[i][j] == True means s[i:j+1] is a palindrome
        for i in reversed(range(l)):
            for j in range(i, l):
                if s[i] == s[j] and (j - i < 2 or dp[i+1][j-1]):
                    dp[i][j] = True
        return sum([v.count(True) for v in dp])
        
        
Two pointers:

class Solution:
    def extend(self, s, i, j, n):
        res = 0
        while i >= 0 and j < n and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res
    
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            res += self.extend(s, i, i, n)
            res += self.extend(s, i, i+1, n)
        return res