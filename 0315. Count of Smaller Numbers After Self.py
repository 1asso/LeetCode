Segment Tree - O(NlogM):
  
class Solution:
    def query(self, l, r, tree, size):
        # return sum of [l, r)
        l, r = l + size, r + size # shift the index to the leaf
        res = 0
        while l < r:
            # if l is a right node
            # bring its value and move to the right node
            if l % 2:
                res += tree[l]
                l += 1
            # move to parent
            l //= 2
            # if r is a right node
            # move to the left node and bring its value
            if r % 2:
                r -= 1
                res += tree[r]
            # move to parent
            r //= 2
        return res
    
    def update(self, index, tree, size):
        index += size  # shift the index to the leaf
        # udpate from leaf to root
        tree[index] += 1 
        while index > 1:
            index //= 2
            tree[index] = tree[index * 2] + tree[index * 2 + 1]
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10 ** 4  # offset negative to non-negative
        size = 2 * offset + 1  # total possible values in nums
        tree = [0] * 2 * size
        res = []
        for num in reversed(nums):
            smaller_count = self.query(0, num + offset, tree, size)
            res.append(smaller_count)
            self.update(num + offset, tree, size)
        return res[::-1]
      
      
Binary Indexed Tree - O(NlogM):
 
class Solution:
    def query(self, bit, index):
        # return sum of [0, index)
        res = 0
        while index >= 1:
            res += bit[index]
            index -= index & -index
        return res
    
    def update(self, index, bit, size):
        index += 1  # index in BIT is 1 more than the original index
        while index < size:
            bit[index] += 1
            index += index & -index

    def countSmaller(self, nums: List[int]) -> List[int]:
        offset = 10 ** 4  # offset negative to non-negative
        size = 2 * offset + 1  # total possible values in nums
        bit = [0] * size
        res = []
        for num in reversed(nums):
            smaller_count = self.query(bit, num + offset)
            res.append(smaller_count)
            self.update(num + offset, bit, size)
        return res[::-1]
