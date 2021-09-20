class Solution:
    def backtracking(self, nums, path, res, index):
        res.append(path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, path, res, i+1)
            path.pop()
            
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtracking(nums, [], res, 0)
        return res