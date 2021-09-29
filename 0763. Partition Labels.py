class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {c:None for c in string.ascii_lowercase}     
        for i in range(len(s)):
            if not d[s[i]]:
                d[s[i]] = [i, i]
            else:
                d[s[i]][1] = i
        l = [v for v in d.values() if v]
        l.sort(key=lambda x: x[0])
        res = []
        last = 0
        for i in range(1, len(l)):
            if l[i][0] < l[i-1][1]:
                l[i][1] = max(l[i][1], l[i-1][1])
            else:
                res.append(l[i][0]-last)
                last = l[i][0]
        res.append(len(s)-last)
        return res
        
        
OR:

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hash = [0] * 26
        for i in range(len(s)):
            hash[ord(s[i])-ord('a')] = i
        dist = 0, 0
        res = []
        for i in range(len(s)):
            dist = dist[0], max(hash[ord(s[i])-ord('a')], dist[1])
            if dist[1] == i:
                res.append(dist[1]-dist[0]+1)
                dist = i+1, 0
        return res