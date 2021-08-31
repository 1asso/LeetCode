class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        low, high, mid1, mid2 = 0, len(nums1), 0, 0
        length = int((len(nums1) + len(nums2) + 1) / 2)

        while low <= high:
            mid1 = int((low + high + 1) / 2)
            mid2 = length - mid1

            if mid1 > 0 and nums1[mid1-1] > nums2[mid2]:
                high = mid1 - 1
            elif mid1 < len(nums1) and nums1[mid1] < nums2[mid2-1]:
                low = mid1 + 1
            else:
                break
                
        if mid1 == 0:
            maxOfLeft = nums2[mid2-1]
        elif mid2 == 0:
            maxOfLeft = nums1[mid1-1]
        else:
            maxOfLeft = max(nums1[mid1-1], nums2[mid2-1])
            
        if (len(nums1) + len(nums2)) % 2:
            return maxOfLeft
        
        if mid1 == len(nums1):
            minOfRight = nums2[mid2]
        elif mid2 == len(nums2):
            minOfRight = nums1[mid1]
        else:
            minOfRight = min(nums1[mid1], nums2[mid2])
            
        return (maxOfLeft + minOfRight) / 2
            