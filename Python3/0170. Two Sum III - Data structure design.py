class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.num = {}

        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.num[number] = len(self.data)
        self.data.append(number)



    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for j in range(len(self.data)):
            if value-self.data[j] in self.num and self.num[value-self.data[j]]!=j:
                return True
        
        return False
    
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.data = []
        

#     def add(self, number: int) -> None:
#         """
#         Add the number to an internal data structure..
#         """
#         self.data.append(number)
#         self.data.sort()
        
        

#     def find(self, value: int) -> bool:
#         """
#         Find if there exists any pair of numbers which sum is equal to the value.
#         """
#         i = 0
#         j = len(self.data) - 1

#         while i<j:
#             if self.data[i] + self.data[j] < value:
#                 i += 1
#             elif self.data[i] + self.data[j] > value:
#                 j -= 1
#             else:
#                 return True
        
#         return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
