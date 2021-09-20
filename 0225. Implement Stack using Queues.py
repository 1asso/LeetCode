class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.appendleft(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q1) > 1:
            self.q2.appendleft(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
        return self.q2.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        res = self.pop()
        self.push(res)
        return res
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()