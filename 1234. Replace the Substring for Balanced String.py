class Solution:
    def balancedString(self, s: str) -> int:
        counter = Counter(s)
        i, n, res = 0, len(s), len(s)
        for j, c in enumerate(s):
            counter[c] -= 1
            while i < n and all(counter[c] <= n // 4 for c in 'QWER'):
                if i > j:
                    return 0
                res = min(res, j - i + 1)
                counter[s[i]] += 1
                i += 1
        return res