DP:

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [height[0]] * len(height)
        max_right = [height[-1]] * len(height)
        res = 0
    
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i-1])
        for i in reversed(range(len(height)-1)):
            max_right[i] = max(height[i], max_right[i+1])
        
        for i in range(len(height)):
            res += min(max_left[i], max_right[i]) - height[i]
        return res
        

Monotonic stack:

class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        mono_st = [0]
        for i in range(1, len(height)):
            while mono_st and height[mono_st[-1]] < height[i]:
                index = mono_st.pop()
                if mono_st:
                    res += (min(height[i], height[mono_st[-1]]) \
                        - height[index]) * (i - mono_st[-1] - 1)
            mono_st.append(i)
        return res