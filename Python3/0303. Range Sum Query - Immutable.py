class NumArray:

    def __init__(self, nums: List[int]):
        self.temp = [0]
        for i in nums:
            self.temp.append(self.temp[-1]+i)

    def sumRange(self, i: int, j: int) -> int:
        return self.temp[j+1]-self.temp[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
