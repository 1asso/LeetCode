class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        mono_st = []
        for i in range(2 * len(nums)):
            while mono_st and nums[mono_st[-1]] < nums[i % len(nums)]:
                res[mono_st.pop()] = nums[i % len(nums)]
            if i < len(nums):
                mono_st.append(i)
        return res