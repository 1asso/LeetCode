class Solution:
    def backtracking(self, nums, path, res, index):
        s = set()
        if len(path) >= 2:
            res.append(path[:])
        for i in range(index, len(nums)):
            if nums[i] in s:
                continue
            s.add(nums[i])
            if not path or nums[i] >= path[-1]:
                path.append(nums[i])
                self.backtracking(nums, path, res, i+1)
                path.pop()
                
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res, 0)
        return res