class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur, pre, res = 0, 0, 1 # first val counts
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if cur != 0 and pre * cur <= 0:
                res += 1
                pre = cur
        return res