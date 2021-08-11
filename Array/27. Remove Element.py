class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        last = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[last] = nums[i]
                last += 1
        return last