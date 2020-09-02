import queue
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()

        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.deque:
            return -1
        
        ans = self.queue.get()

        if ans == self.deque[0]:
            self.deque.popleft()
        
        return ans

    # def __init__(self):
    #     self.max_val = -1
    #     self.arr = []

    # def max_value(self) -> int:
    #     return self.max_val

    # def push_back(self, value: int) -> None:
    #     if value > self.max_val:
    #         self.max_val = value
        
    #     self.arr.append(value)

    # def pop_front(self) -> int:
    #     if not self.arr:
    #         return -1
    #     else:
    #         if self.arr[0] == self.max_val:
    #             self.max_val = max(self.arr[1:]) if len(self.arr)>1 else -1
    #         return self.arr.pop(0)


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
