class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target > nums[-1] or target < nums[0]:
            return -1
        l = 0
        r = len(nums)
        
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        
        return -1