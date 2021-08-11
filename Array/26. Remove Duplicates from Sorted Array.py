class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 1
        for i in range(0, len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[last] = nums[i+1]
                last += 1
        return last