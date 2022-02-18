class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        last = self.nums[-1]
        idx = self.pos[val]
        self.nums[idx] = last
        self.pos[last] = idx
        self.nums.pop()
        self.pos.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()