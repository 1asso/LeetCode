class Solution:
    def backtracking(self, nums, path, res):
        if len(path) == len(nums):
            res.append(path[:])
        else:
            for i in range(len(nums)):
                if not nums[i] in path:
                    path.append(nums[i])
                    self.backtracking(nums, path, res)
                    path.pop()
                    
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res)
        return res