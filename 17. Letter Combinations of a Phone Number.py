class Solution:
    def backtracking(self, l, res, path):
        if len(path) == len(l):
            if len(path):
                res.append(''.join(path))
            return
        ll = l[len(path)]
        for i in range(0, len(ll)):
            path.append(ll[i])
            self.backtracking(l, res, path)
            path.pop()
            
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                  '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        l = [letters[c] for c in digits]
        res = []
        self.backtracking(l, res, [])
        return res