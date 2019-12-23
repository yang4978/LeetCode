class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        res = duration if timeSeries else 0
        l = len(timeSeries)

        for i in range(1,l):
            res += min(timeSeries[i]-timeSeries[i-1],duration)
        
        return res
