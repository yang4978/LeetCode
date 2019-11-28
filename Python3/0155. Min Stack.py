class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_value = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_value==[] or self.min_value[-1]>=x:
            self.min_value.append(x)

    def pop(self) -> None:
        if self.stack.pop()==self.min_value[-1]:
            self.min_value.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_value[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
