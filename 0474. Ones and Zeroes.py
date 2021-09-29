class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for s in strs:
            ones = s.count('1')
            zeros = s.count('0')
            for j in reversed(range(zeros, m+1)):
                for k in reversed(range(ones, n+1)):
                    dp[j][k] = max(dp[j][k], dp[j-zeros][k-ones] + 1)
        return dp[-1][-1]