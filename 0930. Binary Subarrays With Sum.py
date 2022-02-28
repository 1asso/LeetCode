Prefix Sums (also works where negative vals exist):

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        counter = Counter({0: 1})
        prefix_sum, res = 0, 0
        # prefix_sum_1 = sum(nums[0] ~ nums[j])
        # goal == sum(nums[i + 1] ~ nums[j])
        # prefix_sum_0 = sum(nums[0] ~ nums[i]) == prefix_sum_1 - goal
        # count how many i-s satisfy prefix_sum_0
        for num in nums:
            prefix_sum += num
            res += counter[prefix_sum - goal]
            counter[prefix_sum] += 1
        return res
        

Sliding Window:

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def at_most(k):
            if k < 0:
                 return 0
            i = res = 0
            for j in range(len(nums)):
                k -= nums[j]
                while k < 0:
                    k += nums[i]
                    i += 1
                res += j - i + 1
            return res
        return at_most(goal) - at_most(goal - 1)