DP:

class Solution:    
    def longestPalindromeSubseq(self, s: str) -> int:
        s1, s2, l = s, s[::-1], len(s) + 1
        dp = [[0] * l for _ in range(l)]
        for i in range(1, l):
            for j in range(1, l):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]
        
        
OR (faster):

class Solution:    
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        dp = [[0] * l for _ in range(l)]
        for i in range(l):
            dp[i][i] = 1
        for i in reversed(range(l)):
            for j in range(i+1, l):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        return dp[0][-1]