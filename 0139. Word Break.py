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
        
        
OR:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if s[i-len(word)+1:i+1] == word and (dp[i-len(word)] or i < len(word)):
                    dp[i] = True
        return dp[-1]