class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: int(a / b),
        }
        stack = []
        for c in tokens:
            if c in operators.keys():
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(operators[c](a, b))
            else:
                stack.append(c)
        return stack.pop()