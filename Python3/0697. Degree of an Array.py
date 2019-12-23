class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        start = {}
        end = {}
        times = {}
        max_value = 0

        l = len(nums)

        for i in range(l):
            if nums[i] not in start:
                start[nums[i]] = i
            end[nums[i]] = i
            if nums[i] not in times:
                times[nums[i]] = 1
            else:
                times[nums[i]] += 1
            max_value = times[nums[i]] if times[nums[i]]>=max_value else max_value

        res = l

        for key,value in times.items():
            if value == max_value:
               res = min(res,end[key]-start[key]+1)

        return res         
        
