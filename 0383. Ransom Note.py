class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_m = Counter(list(magazine))
        for c in ransomNote:
            dict_m[c] -= 1
            if dict_m[c] < 0:
                return False
        return True