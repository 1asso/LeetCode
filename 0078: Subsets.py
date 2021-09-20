class Solution:
    def backtracking(self, nums, path, res, index):
        res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, path, res, i+1)
            path.pop()
            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtracking(nums, [], res, 0)
        return res