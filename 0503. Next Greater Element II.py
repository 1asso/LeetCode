class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_extended = nums + nums
        res = [-1] * len(nums)
        mono_st = []
        for i in range(len(nums_extended)):
            while mono_st and nums_extended[mono_st[-1]] < nums_extended[i]:
                index = mono_st.pop()
                if index < len(nums):
                    res[index] = nums_extended[i]
            mono_st.append(i)
        return res