DP:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        leftIndex = [-1] * N
        rightIndex = [N] * N
        res = 0
        
        for i in range(1, N):
            t = i - 1
            while t >= 0 and heights[t] >= heights[i]:
                t = leftIndex[t]
            leftIndex[i] = t
        
        for i in reversed(range(N-1)):
            t = i + 1
            while t < N and heights[t] >= heights[i]:
                t = rightIndex[t]
            rightIndex[i] = t
            
        for i in range(N):
            res = max(res, heights[i] * (rightIndex[i] - leftIndex[i] - 1))
        return res
        
        
 Monotonic Stack:
 
 class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        mono_st = []
        heights = [0] + heights + [0]
        
        for i in range(len(heights)):
            while mono_st and heights[mono_st[-1]] > heights[i]:
                t = mono_st.pop()
                area = max(area, heights[t] * (i - mono_st[-1] - 1))
            mono_st.append(i)
        return area