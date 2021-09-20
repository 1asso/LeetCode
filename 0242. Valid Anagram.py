class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = Counter(s)
        dict_t = Counter(t)
        return dict_s == dict_t