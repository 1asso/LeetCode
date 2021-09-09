class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        counter = Counter([-(n1 + n2) for n1 in nums1 for n2 in nums2])
        return sum([counter[n3 + n4] for n3 in nums3 for n4 in nums4])