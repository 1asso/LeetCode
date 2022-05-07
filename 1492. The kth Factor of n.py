Brute force O(N):

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1, n + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
        return -1
        

Heap O(sqrt(N) * logk):

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                heappush(heap, -i)
                if i != n // i:
                    heappush(heap, -(n // i))
            while len(heap) > k:
                heappop(heap)
        return -heap[0] if k == len(heap) else -1
        
        
Math O(sqrt(N)):

class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        divisors = []
        sqrtn = int(sqrt(n))
        for i in range(1, sqrtn + 1):
            if n % i == 0:
                k -= 1
                if k == 0:
                    return i
                divisors.append(i)
        if sqrtn * sqrtn == n:
            k += 1
        return n // divisors[len(divisors) - k] if k <= len(divisors) else -1