Brute Force (time limit exceeded):

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        n_dict = collections.defaultdict(list)
        for k, v in enumerate(nums2):
            n_dict[v].append(k)
        
        for k, v in enumerate(nums1):
            for j in n_dict[v]:
                l = 0
                while max(k, j) + l < len(nums1) and \
                    nums1[k+l] == nums2[j+l]:
                    l += 1
                res = max(res, l)
        return res
        

DP:

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1)+1)]
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
        return max(map(max, dp))