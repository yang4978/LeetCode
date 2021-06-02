class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = [0]
        mod = dict()
        for i in range(len(nums)):
            n = nums[i]
            x = prefix[-1] + n
            prefix.append(x)
            if((i != 0 and x % k == 0) or (x % k in mod and i - mod[x % k] > 1)):
                return True
            elif(x % k not in mod):
                mod[x % k] = i

        return False
