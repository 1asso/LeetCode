class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_streak = 0
        s = set(nums)
        for num in s:
            if num - 1 not in s:
                cur_streak = 1
                cur_num = num + 1
                while cur_num in s:
                    cur_streak += 1
                    cur_num += 1
                longest_streak = max(longest_streak, cur_streak)
        return longest_streak