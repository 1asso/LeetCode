Solution 1: 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)
        
        dict_s = {}
        l = 0
        ans = float("inf"), None, None
        
        for r in range(len(s)):
            c = s[r]
            dict_t[c] -= 1
            
            if dict_t[c] == 0:
                required -= 1
                
            while l <= r and not required:
                c = s[l]
                
                if r - l + 1 < ans[0]:
                    ans = r - l + 1, l, r
                
                l += 1
                dict_t[c] += 1
                if dict_t[c] > 0:
                    required += 1
                
        return s[ans[1]:ans[2] + 1] if ans[0] <= len(s) else ""
                
                
        
Solution 2(filtered_s):


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict_t = Counter(t)
        required = len(dict_t)
        
        filtered_s = []
        for i, c in enumerate(s):
            if c in dict_t:
                filtered_s.append((i, c))
        
        dict_s = {}
        l = 0
        ans = float("inf"), None, None
        
        for r in range(len(filtered_s)):
            c = filtered_s[r][1]
            dict_t[c] -= 1
            
            if dict_t[c] == 0:
                required -= 1
                
            while l <= r and not required:
                c = filtered_s[l][1]
                
                end = filtered_s[r][0]
                start = filtered_s[l][0]
                
                if end - start + 1 < ans[0]:
                    ans = end - start + 1, start, end
                
                l += 1
                dict_t[c] += 1
                if dict_t[c] > 0:
                    required += 1
                
        return s[ans[1]:ans[2] + 1] if ans[0] <= len(s) else ""