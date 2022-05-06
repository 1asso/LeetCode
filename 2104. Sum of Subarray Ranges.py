Similar to Q907:

class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def minmax(func):
            st, N = [], len(nums)
            l, r = [-1] * N, [N] * N
            for i in range(N):
                while st and func(nums[i], nums[st[-1]]):
                    r[st.pop()] = i
                if st: l[i] = st[-1]
                st.append(i)
            return sum(nums[i] * (i - l[i]) * (r[i] - i) for i in range(N))
        return minmax(lambda x, y: x > y) - minmax(lambda x, y: x < y)