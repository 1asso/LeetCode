class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = None
        
        for index in range(len(nums) - 2):
            if index > 0 and nums[index] == nums[index-1]:
                continue
            begin, end = index + 1, len(nums) - 1
            
            while begin < end:
                s = nums[index] + nums[begin] + nums[end]
                
                if s < target:
                    begin += 1
                elif s > target:
                    end -= 1
                else:
                    return s
                
                if result == None or abs(s - target) < abs(result - target):
                    result = s
                    
        return result