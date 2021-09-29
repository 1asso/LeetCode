class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        res = 0
        min_price = prices[0]
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > fee:
                res += prices[i] - min_price - fee
                min_price = prices[i] - fee
        return res