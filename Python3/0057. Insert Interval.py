class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        l = len(intervals)
        if l==0:
            return [newInterval]
        index = -1
        i = 0
        while i<l:
            while i<l and (newInterval[0]<=intervals[i][0]<=newInterval[1] or newInterval[0]<=intervals[i][1]<=newInterval[1] or (newInterval[0]>intervals[i][0] and newInterval[1]<intervals[i][1])):

                if index==-1:
                    index = i
                    i += 1

                else:
                    start,end = intervals.pop(i)
                    newInterval[0] = min(newInterval[0],start)
                    newInterval[1] = max(newInterval[1],end)
                    l -= 1
            
            i += 1

        if index == -1:
            if intervals[-1][1]<newInterval[0]:
                intervals.append(newInterval)
            elif intervals[0][0]>newInterval[1]:
                intervals = [newInterval] + intervals
            else:
                for i in range(l-1):
                    if intervals[i][1]<newInterval[0] and intervals[i+1][0]>newInterval[1]:
                        intervals.insert(i+1,newInterval)
                        break
        
        else:
            intervals[index][0] = min(intervals[index][0],newInterval[0])
            intervals[index][1] = max(intervals[index][1],newInterval[1])

        return intervals
