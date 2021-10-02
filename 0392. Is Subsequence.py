Two pointers:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                l += 1
            r += 1
        return l == len(s)
        
        
DP:

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len1, len2 = len(s) + 1, len(t) + 1
        dp = [[0] * len2 for _ in range(len1)]
        
        for i in range(1, len1):
            for j in range(1, len2):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[-1][-1] + 1 == len1