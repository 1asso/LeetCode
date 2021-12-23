class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_so_far = cur_max = start = 0
        hashtb = {}
        for i, v in enumerate(s):
            if v in hashtb and hashtb[v] >= start:
                max_so_far = max(max_so_far, cur_max)
                cur_max = i - hashtb[v]
                start = hashtb[v] + 1
            else:
                cur_max += 1
            hashtb[v] = i
        return max(cur_max, max_so_far)