class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if not points:
        #     return 0

        # points.sort()

        # res = 1

        # start, end = points[0]

        # for i in points[1:]:
        #     ts, te = i
        #     if end >= ts:
        #         start = ts
        #         end = min(te,end)
        #     else:
        #         res += 1
        #         start, end = ts, te
        # return res

        # start, end = points[0]


        if not points:
            return 0

        points.sort()

        res = 1

        end = points[0][1]

        for i in points[1:]:
            ts, te = i
            if end >= ts:
                end = min(te,end)
            else:
                res += 1
                end = te
        return res
