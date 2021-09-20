class Solution:
    def backtracking(self, candidates, target, res, path, cur_index):
        s = sum(path)
        if s == target:
            res.append(path[:])
        for i in range(cur_index, len(candidates)):
                if s + candidates[i] > target:
                    return
                path.append(candidates[i])
                self.backtracking(candidates, target, res, path, i)
                path.pop()   

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        self.backtracking(candidates, target, res, [], 0)
        return res