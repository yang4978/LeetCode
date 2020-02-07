class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]
        self.arr = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        self.arr = self.original[:]
        return self.arr

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        for i in range(len(self.arr)):
            swap = random.randrange(i,len(self.arr))
            self.arr[swap],self.arr[i] = self.arr[i],self.arr[swap]
        
        return self.arr
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
