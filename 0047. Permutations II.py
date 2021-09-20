class Solution:
    def backtracking(self, nums, path, res, used):
        s = set()
        if len(path) == len(nums):
            res.append(path[:])
        else:
            for i in range(len(nums)):
                if used[i] or nums[i] in s:
                    continue
                s.add(nums[i])
                path.append(nums[i])
                used[i] = 1
                self.backtracking(nums, path, res, used)
                used[i] = 0
                path.pop()
                
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = {i:0 for i in range(len(nums))}
        self.backtracking(nums, [], res, used)
        return res