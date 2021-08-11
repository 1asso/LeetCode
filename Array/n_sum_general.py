class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def nSum(l, r, target, N, result, results):
            if N < 2 or target < nums[l] * N or target > nums[r] * N:
                return
            if N == 2:
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        results.append(result + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                for i in range(l, r - N + 2):
                    if i > l and nums[i] == nums[i-1]:
                        continue
                    nSum(i+1, r, target-nums[i], N-1, result+[nums[i],], results)
        
        results = []
        nums.sort()
        if len(nums) >= 4:
            nSum(0, len(nums)-1, target, 4, [], results)
        return results