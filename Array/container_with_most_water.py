class Solution:
    def maxArea(self, height: List[int]) -> int:
        begin, end = 0, len(height) - 1
        maxVolume = 0
        while begin < end:
            if height[begin] < height[end]:
                maxVolume = max(maxVolume, height[begin] * (end - begin))
                begin += 1
            else:
                maxVolume = max(maxVolume, height[end] * (end - begin))
                end -= 1
                
        return maxVolume