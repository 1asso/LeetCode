class Solution:
    def backtracking(self, res, path, n, k, start_index):
        if len(path) == k:
            res.append(path)
        for i in range(start_index, n+1):
            self.backtracking(res, path+[i], n, k, i+1)

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(res, [], n, k, 1)
        return res
 
       
Pruning:

class Solution:
    def backtracking(self, res, path, n, k, start_index):
        if len(path) == k:
            res.append(path[:])
            return
        for i in range(start_index, n-(k-len(path))+2):
            path.append(i)
            self.backtracking(res, path, n, k, i+1)
            path.pop()

    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtracking(res, [], n, k, 1)
        return res