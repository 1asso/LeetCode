DP:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[[0, 0], [0, 0], [0, 0]] for _ in range(len(prices))]
        dp[0][0], dp[0][1], dp[0][2] = [-prices[0], 0], [-prices[0], 0], [0, 0]
        # 0th price: [trans0 + hold, trans0 + not hold], [trans1 + hold, trans1 + not hold]
        dp[1][0] = [-min(prices[:2]), 0]
        dp[1][1] = [-min(prices[:2]), max(0, prices[1]-prices[0])]
        dp[1][2] = [0, max(0, prices[1]-prices[0])]

        for i in range(2, len(prices)):
            dp[i][0] = [max(dp[i-1][0][0], -prices[i]), 0]
            dp[i][1] = [max(dp[i-1][1][1] - prices[i], dp[i-1][1][0]), \
                       max(dp[i-1][0][0] + prices[i], dp[i-1][1][1])]
            dp[i][2] = [0, max(dp[i-1][1][0] + prices[i], dp[i-1][2][1])]
        return max([max(i) for i in dp[-1]])


Better one:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 4 for _ in range(len(prices))]
        # [trans0 hold1, trans1 hold0, trans1 hold1, trans2 hold0]
        dp[0][0], dp[0][2] = -prices[0], -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(-prices[i], dp[i-1][0])
            dp[i][1] = max(dp[i-1][0] + prices[i], dp[i-1][1])
            dp[i][2] = max(dp[i-1][1] - prices[i], dp[i-1][2])
            dp[i][3] = max(dp[i-1][2] + prices[i], dp[i-1][3])
        return dp[-1][3]