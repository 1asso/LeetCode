class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most(k):
            counter = {}
            res = i = 0
            for j in range(len(nums)):
                counter[nums[j]] = counter.get(nums[j], 0) + 1
                while len(counter) > k:
                    counter[nums[i]] -= 1
                    if counter[nums[i]] == 0:
                        counter.pop(nums[i])
                    i += 1
                res += j - i + 1
            return res
        return at_most(k) - at_most(k - 1)