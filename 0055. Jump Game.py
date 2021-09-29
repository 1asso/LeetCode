class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        l, r = 0, 0
        for r in range(len(nums)):
            if nums[r] == 0:
                flag = True
                for l in reversed(range(r)):
                    if nums[l] > r - l or nums[l] == len(nums) - l - 1:
                        flag = False
                        break
                if flag: return False
        return True
        
        
OR:

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        cover = nums[0]
        i = 0
        while i <= cover:
            cover = max(nums[i] + i, cover)
            if cover >= len(nums) - 1:
                return True
            i += 1
        return False