class Solution:
    def jump(self, nums: List[int]) -> int:
        res, i, start, end = 0, 0, 0, 0
        while end < len(nums) - 1:
            i = start
            tmp = end
            while i <= end:
                if nums[i] + i >= tmp:
                    start, tmp = i + 1, nums[i] + i
                i += 1
            end = tmp
            res += 1
        return res