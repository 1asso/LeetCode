class Solution:
    def numSquares(self, n: int) -> int:
        ps = [i * i for i in range(1, int(sqrt(n))+1)]
        dp = [n + 1] * (n + 1)
        dp[0] = 0
        for cand in ps:
            for j in range(cand, n+1):
                dp[j] = min(dp[j], dp[j-cand]+1)
        return dp[-1]