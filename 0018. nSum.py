class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        def nSum(target, path, N, index):
            if nums[index] * N > target or nums[-1] * N < target:
                return
            if N == 2:
                l, r = index, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s < target:
                        l += 1
                    elif s > target:
                        r -= 1
                    else:
                        res.append(path + [nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
            else:
                for i in range(index, len(nums)-N+1):
                    if i > index and nums[i] == nums[i-1]:
                        continue
                    nSum(target-nums[i], path+[nums[i]], N-1, i+1)
        nSum(target, [], 4, 0)
        return res