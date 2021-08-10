class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for index in range(len(nums) - 2):
            if nums[index] > 0:
                break
            if index > 0 and nums[index] == nums[index-1]:
                continue
            begin, end = index + 1, len(nums) - 1
            
            while begin < end:
                s = nums[index] + nums[begin] + nums[end]
                
                if s < 0:
                    begin += 1
                elif s > 0:
                    end -= 1
                else:
                    results.append([nums[index], nums[begin], nums[end]])
                    while begin < end and nums[begin] == nums[begin+1]:
                        begin += 1
                    while begin < end and nums[end] == nums[end-1]:
                        end -= 1
                    begin += 1
                    end -= 1
                
        return results