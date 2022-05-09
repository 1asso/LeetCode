class Solution:
    def calculate(self, s: str) -> int:
        num, st, op = 0, [], '+'
        s += '+'
        ops = {
            '+': lambda num: st.append(num),
            '-': lambda num: st.append(-num),
            '*': lambda num: st.append(st.pop() * num),
            '/': lambda num: st.append(int(st.pop() / num)),
            'Invalid': lambda num: num  # Do nothing here
        }
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)
            elif c in ops:
                ops[op](num)
                num, op = 0, c
            elif c == '(':
                st.append(op)
                op = '+'
            else:
                ops[op](num)
                num = 0
                while st[-1] not in ops:
                    num += st.pop()
                ops[st.pop()](num)
                num, op = 0, 'Invalid'
        return sum(st)
        
        
        
        
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
