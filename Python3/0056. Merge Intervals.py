class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if(intervals==[]):return intervals
        intervals.sort(reverse=True)
        res = [intervals.pop()]
        while(intervals!=[]):
            item = intervals.pop()
            r = res[-1][:]
            if(r[1]>=item[0]):
                r[0] = min(r[0],item[0])
                r[1] = max(r[1],item[1])
                res[-1] = r[:]
            else:
                res.append(item)
        return res

#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort()
#         if(len(intervals)<=1): return intervals
        
#         result = []
#         l = intervals[0][0]
#         h = intervals[0][1]

#         for i in range(1,len(intervals)):
#             if(h>=intervals[i][0]):
#                 l = min(l,intervals[i][0])
#                 h = max(h,intervals[i][1])
#             else:
#                 result.append([l,h])
#                 l = intervals[i][0]
#                 h = intervals[i][1]
#         result.append([l,h])
#         return result
