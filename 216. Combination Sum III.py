class Solution:
    def sum(self, k, n, res, path, cur_index):
        if len(path) == k:
            if sum(path) == n:
                res.append(path[:])
            return
        for i in range(cur_index, 10-(k-len(path))+1):
            path.append(i)
            self.sum(k, n, res, path, i+1)
            path.pop()
        
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        self.sum(k, n, res, [], 1)
        return res