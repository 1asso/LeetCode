DP:

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for word in wordDict:
                size = len(word)
                if i >= size - 1 and s[i - size + 1: i + 1] == word:
                    if i - size + 1 == 0:
                        dp[i].append(word)
                    else:
                        for l in dp[i - size]:
                            dp[i].append(l + ' ' + word)
        return dp[-1]
        

DFS & Memorization:

# sentences(i) returns a list of all sentences that can be built from the suffix s[i:].
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = []
                for j in range(i + 1, len(s) + 1):
                    word = s[i:j]
                    if word in wordDict:
                        for tail in sentences(j):
                            memo[i].append(word + (tail and ' ' + tail))
            return memo[i]
        return sentences(0)