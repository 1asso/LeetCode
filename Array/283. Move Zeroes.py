class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        for i in range(1, len(nums)):
            if nums[last] != 0:
                last += 1
            if nums[i] == 0:
                continue
            nums[last], nums[i] = nums[i], nums[last]844. Backspace String Compare