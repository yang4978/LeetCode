class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_value = sum(nums[:k])
        temp = sum_value
        l = len(nums)
        for i in range(l-k):
            sum_value += nums[i+k] - nums[i]
            temp = max(temp,sum_value)
        return temp/k
