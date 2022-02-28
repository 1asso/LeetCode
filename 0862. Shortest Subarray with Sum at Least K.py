class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        increasing = deque()
        res = N + 1
        presum = [0] * (N + 1)
        for i in range(N):
            presum[i + 1] = presum[i] + nums[i]
        for i in range(N + 1):
            while increasing and presum[i] - presum[increasing[0]] >= k:
                res = min(res, i - increasing.popleft())
            while increasing and presum[i] <= presum[increasing[-1]]:
                increasing.pop()
            increasing.append(i)
        return res if res <= N else -1