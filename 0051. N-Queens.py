class Solution:    
    def backtracking(self, n, path, res, queens, sub, sum):
        if len(path) == n:
            res.append(['.'*path[i]+'Q'+'.'*(n-path[i]-1) for i in range(n)])
        else:
            r = len(queens)
            for c in range(n):
                if c not in queens and r-c not in sub and r+c not in sum:
                    self.backtracking(n, path+[c], res, queens+[c], sub+[r-c], sum+[r+c])
                    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.backtracking(n, [], res, [], [], [])
        return res
        
        
OR:

class Solution:
    def check(self, index, path):
        row = len(path)
        for r, i in enumerate(path):
            if i == index:
                return False
            if r + i == row + index or r - i == row - index:
                return False
        return True
    
    def backtracking(self, n, path, res):
        if len(path) == n:
            res.append(['.'*path[i]+'Q'+'.'*(n-path[i]-1) for i in range(n)])
        else:
            for i in range(n):
                if self.check(i, path):
                    path.append(i)
                    self.backtracking(n, path, res)
                    path.pop()
                    
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        self.backtracking(n, [], res)
        return res