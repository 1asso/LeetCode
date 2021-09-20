class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mono_st, d = [], {}
        for i in range(len(nums2)):
            while mono_st and mono_st[-1] < nums2[i]:
                d[mono_st.pop()] = nums2[i]
            mono_st.append(nums2[i])
        return [d.get(x, -1) for x in nums1]