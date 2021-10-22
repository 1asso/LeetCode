O(nlogn):

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        mid = len(nums[::2])
        nums[::2], nums[1::2] = nums[:mid][::-1], nums[mid:][::-1]
            
            
O(n):

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mid = median(nums)
        
        def mapping(i):
            mid = len(nums) // 2
            if i < mid:
                return 1 + i * 2
            else:
                return (i - mid) * 2
                
        # three-way partitioning
        
        i, j, k = 0, 0, len(nums) - 1
        while j <= k:
            if nums[mapping(j)] > mid:
                nums[mapping(i)], nums[mapping(j)] = nums[mapping(j)], nums[mapping(i)]
                i += 1
                j += 1
            elif nums[mapping(j)] < mid:
                nums[mapping(j)], nums[mapping(k)] = nums[mapping(k)], nums[mapping(j)]
                k -= 1
            else:
                j += 1