DP:

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        N = len(heights)
        l = [-1] * N
        r = [N] * N
        res = 0
        for i in range(N):
            t = i - 1
            while t >= 0 and heights[t] >= heights[i]:
                t = l[t]
            l[i] = t
        for i in reversed(range(N)):
            t = i + 1
            while t < N and heights[t] >= heights[i]:
                t = r[t]
            r[i] = t
        for i in range(N):
            res = max(res, heights[i] * (r[i] - l[i] - 1))
        return res
        
        
Monotonic Stack:
 
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = []
        area = 0
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                last = st.pop()
                area = max(area, heights[last] * (i - st[-1] - 1))
            st.append(i)
        return area