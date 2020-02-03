from queue import Queue

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = Queue()
        self.q2 = Queue()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q1.put(x)
        self.top_val = x

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while self.q1.qsize()>1:
            self.top_val = self.q1.get()
            self.q2.put(self.top_val)
        
        res = self.q1.get()
        
        self.q1,self.q2 = self.q2,self.q1

        return res

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.top_val
        
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return self.q1.empty() and self.q2.empty()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
