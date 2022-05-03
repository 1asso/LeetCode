Monotonic stack (similar to Q84):

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        N = len(matrix[0])
        heights = [0] * (N + 1)
        area = 0
        for row in matrix:
            st = [-1]
            for i in range(N):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            for i in range(N + 1):
                while st and heights[st[-1]] > heights[i]:
                    last = st.pop()
                    area = max(area, heights[last] * (i - st[-1] - 1))
                st.append(i)
        return area