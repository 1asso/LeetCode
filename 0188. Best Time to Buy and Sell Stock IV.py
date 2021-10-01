class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices:
            return 0
        l_size = 2 * k + 1
        dp = [[0] * (l_size) for _ in range(len(prices))]
        dp[0] = [-prices[0] if i % 2 else 0 for i in range(l_size)]
        for i in range(1, len(prices)):
            for j in range(1, l_size):
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (-1) ** j * prices[i])
        return dp[-1][-1]