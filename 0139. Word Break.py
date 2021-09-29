class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s) + 1)
        for j in range(len(s)+1):
            for word in wordDict:
                l = len(word)
                if j >= l:
                    if s[j-l:j] == word:
                        dp[j] = max(dp[j], dp[j-l] + l)
        return dp[-1] == len(s)