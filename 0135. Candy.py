class Solution:
    def candy(self, ratings: List[int]) -> int:
        nums = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                nums[i] = nums[i-1] + 1
        for i in reversed(range(len(ratings)-1)):
            if ratings[i] > ratings[i+1]:
                nums[i] = max(nums[i], nums[i+1] + 1)
        return sum(nums)