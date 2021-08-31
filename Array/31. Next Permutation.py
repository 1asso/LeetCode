class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i = i-1
        j = i
        i = i - 1
        while j < len(nums):
            if nums[j] <= nums[i]:
                break
            j += 1
        nums[j-1], nums[i] = nums[i], nums[j-1]
        nums[i+1: ] = sorted(nums[i+1: ])