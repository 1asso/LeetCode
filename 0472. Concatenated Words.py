DFS with memo O(NL^3) - N is the number of words and L is the max length of a word:

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        d = set(words)
        memo = {}
        def dfs(word):
            if word in memo:
                return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in d and (suffix in d or dfs(suffix)):
                    memo[word] = True
                    return True
            memo[word] = False
            return False
        res = []
        for word in words:
            if dfs(word):
                res.append(word)
        return res