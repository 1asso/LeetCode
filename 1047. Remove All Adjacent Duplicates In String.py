class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)