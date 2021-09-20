class Solution:
    def backtracking(self, s, path, res, index):
        if index == len(s):
            res.append(path[:])
        else:
            for i in range(index, len(s)):
                p = s[index:i+1]
                if p == p[::-1]:
                    path.append(p)
                    self.backtracking(s, path, res, i+1)
                    path.pop()

    def partition(self, s: str) -> List[List[str]]:
        res = []
        self.backtracking(s, [], res, 0)
        return res