class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        def searchLeft(nums, target):
            l, r = 0, len(nums)
            
            while l < r:
                mid = (l + r) // 2
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        def searchRight(nums, target):
            l, r = 0, len(nums)
            
            while l < r:
                mid = (l + r) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l - 1
        
        l, r = searchLeft(nums, target), searchRight(nums, target)
        return [l, r]