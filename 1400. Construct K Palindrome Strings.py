class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        counter = Counter(s)
        odd_count = 0
        even_count = 0
        for _, v in counter.items():
            if v % 2:
                odd_count += 1
            even_count += v // 2
        return odd_count <= k and even_count * 2 + odd_count >= k