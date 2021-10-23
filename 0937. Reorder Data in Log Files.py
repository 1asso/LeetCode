class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        l = r = len(logs) - 1
        while l >= 0:
            if logs[l].split()[1].isdigit():
                logs[l], logs[r] = logs[r], logs[l]
                r -= 1
            l -= 1
        logs[:r+1] = sorted(logs[:r+1], key=lambda x: (' '.join(x.split()[1:]), x.split()[0]))
        return logs
