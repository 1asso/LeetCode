class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        if len(nums) < 4:
            return
        
        for i in range(len(nums) - 3):
            if target < nums[i] * 4 or target > nums[-1] * 4:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if target - nums[i] < nums[j] * 3 or target - nums[i] > nums[-1] * 3:
                    break
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                begin, end = j + 1, len(nums) - 1
                t = target - nums[i] - nums[j]
                
                while begin < end:
                    s = nums[begin] + nums[end]

                    if s < t:
                        begin += 1
                    elif s > t:
                        end -= 1
                    else:
                        results.append([nums[i], nums[j], nums[begin], nums[end]])
                        while begin < end and nums[begin] == nums[begin+1]:
                            begin += 1
                        while begin < end and nums[end] == nums[end-1]:
                            end -= 1
                        begin +=1
                        end -= 1

        return results