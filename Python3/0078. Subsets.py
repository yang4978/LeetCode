class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = [[]]
        # for i in nums:
        #     result += [j+[i] for j in result]
        # return result
        
        size = len(nums)
        x = 1<<size
        result = []
        for i in range(x):
            temp = []
            for j in range(size):
                if i>>j&1:
                    temp.append(nums[j])
            result.append(temp)
        return result
