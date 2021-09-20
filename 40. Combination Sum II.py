class Solution:
    def backtracking(self, candidates, path, res, target, s, index):
        if s == target:
            res.append(path[:])
        for i in range(index, len(candidates)):
            if s + candidates[i] > target:
                return
            if i > index and candidates[i-1] == candidates[i]:
                continue
            path.append(candidates[i])
            self.backtracking(candidates, path, res, target, s+candidates[i], i+1)
            path.pop()   
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtracking(candidates, [], res, target, 0, 0)
        return res