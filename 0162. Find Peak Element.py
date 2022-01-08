Brute force O(n):

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                return i
        return len(nums) - 1
        

Binary search O(logn):

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        def bisect(l, r):
            if l == r:
                return l
            mid = (l + r) // 2
            if nums[mid] > nums[mid + 1]:
                return bisect(l, mid)
            return bisect(mid + 1, r)
        return bisect(0, len(nums) - 1)