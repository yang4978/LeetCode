class MyHashSet:

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.arr = [0]*(1<<20)


    # def add(self, key: int) -> None:
    #     self.arr[key] = 1

    # def remove(self, key: int) -> None:
    #     self.arr[key] = 0

    # def contains(self, key: int) -> bool:
    #     """
    #     Returns true if this set contains the specified element
    #     """
    #     return self.arr[key] == 1


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.arr = [[] for _ in range(857)]


    def add(self, key: int) -> None:
        if key not in self.arr[key%857]:
            self.arr[key%857].append(key) 

    def remove(self, key: int) -> None:
        if key in self.arr[key%857]:
            self.arr[key%857].pop(self.arr[key%857].index(key))

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        return key in self.arr[key%857]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
