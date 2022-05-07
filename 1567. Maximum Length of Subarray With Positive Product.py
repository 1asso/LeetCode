DP :
# "pos[i]", "neg[i]" represent longest consecutive numbers ending with nums[i] forming a positive/negative product.

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos, neg = 0, 0
        if nums[0] > 0:
            pos = 1
        if nums[0] < 0:
            neg = 1
        res = pos
        for i in range(1, len(nums)):
            if nums[i] > 0:
                pos += 1
                neg = neg + 1 if neg else 0
            elif nums[i] == 0:
                pos, neg = 0, 0
            else:
                pos, neg = neg + 1 if neg else 0, pos + 1
            res = max(res, pos)
        return res