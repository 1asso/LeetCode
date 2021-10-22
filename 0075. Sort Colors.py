class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, i, r = 0, 0, len(nums)-1
        while i <= r:
            if nums[i] < 1:
                nums[l], nums[i] = nums[i], nums[l]
                i += 1
                l += 1
            elif nums[i] > 1:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            else:
                i += 1