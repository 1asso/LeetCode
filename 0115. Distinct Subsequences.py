class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        len1, len2 = len(s) + 1, len(t) + 1
        dp = [[0] * len2 for _ in range(len1)]
        for i in range(len1):
            dp[i][0] = 1
        for i in range(1, len1):
            for j in range(1, min(len2, i+1)):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]