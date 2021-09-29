class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0, 0, 1]
        for i in range(3, n+1):
            dp.append(0)
            for j in range(1, i+1):
                dp[i] = max(dp[i], max(j * dp[i-j], j * (i-j)))
        return dp[-1]