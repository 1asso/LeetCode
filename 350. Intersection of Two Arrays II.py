class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        dict1 = Counter(nums1)
        for num in nums2:
            if dict1[num] > 0:
                res.append(num)
                dict1[num] -= 1
        return res