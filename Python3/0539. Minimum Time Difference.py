class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        time = []
        for i in timePoints:
            k = 60*int(i[:2])+int(i[3:])
            if k in time:
                return 0
            time+=[k]

        time.sort()
        time += [1440+time[0]]
        ans = 1440
        n = len(time)
        for i in range(1,n):
            ans = min(time[i]-time[i-1],ans)
        return ans
