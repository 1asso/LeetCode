class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        set1 = set(nums1)
        for num in nums2:
            if num in set1:
                res.add(num)
        return res
        
        
        
Use & operator (slower

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = Counter(nums1)
        dict2 = Counter(nums2)
        return dict1.keys() & dict2.keys()