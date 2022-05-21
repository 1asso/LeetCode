Similar to Q828:

class Solution:
    def appealSum(self, s: str) -> int:
        index, dp = defaultdict(lambda: -1), [0] * len(s)
        for i, c in enumerate(s):
            j = index[c]
            dp[i] = dp[i - 1] + (i - j)
            index[c] = i
        return sum(dp)