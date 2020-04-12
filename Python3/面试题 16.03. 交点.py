class Solution:
    def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
        x1,y1,x2,y2 = *start1,*end1
        x3,y3,x4,y4 = *start2,*end2
        det = lambda a,b,c,d: a*d - b*c

        D = det(x1-x2,x4-x3,y1-y2,y4-y3)
        P = det(x4-x2,x4-x3,y4-y2,y4-y3)
        Q = det(x1-x2,x4-x2,y1-y2,y4-y2)

        if D:
            lam, eta = P/D, Q/D
            if 0<=lam<=1 and 0<=eta<=1:
                return [lam*x1+(1-lam)*x2, lam*y1+(1-lam)*y2]
            else:
                return []
        
        if P or Q:
            return []

        t1, t2 = sorted([start1,end1]), sorted([start2,end2])

        if t1[1] < t2[0] or t1[0] > t2[1]:
            return []
        
        return max(t1[0],t2[0])

    # def intersection(self, start1: List[int], end1: List[int], start2: List[int], end2: List[int]) -> List[float]:
    #     def line(x1,y1,x2,y2):
    #         a = 1
    #         b = 1
    #         c = 1
    #         if x1 == x2:
    #             b = 0
    #             c = -x1
    #         elif y1 == y2:
    #             a = 0
    #             c = -y1
    #         else:
    #             b = -(x1-x2)/(y1-y2)
    #             c = -x1-b*y1

    #         return (a,b,c)
        
    #     x1,y1,x2,y2 = *start1,*end1
    #     a1,b1,c1 = line(x1,y1,x2,y2)
    #     x3,y3,x4,y4 = *start2,*end2
    #     a2,b2,c2 = line(x3,y3,x4,y4)

    #     if x1 > x2:
    #         x1, x2 = x2, x1
    #     elif x1 == x2:
    #         if y1 > y2:
    #             y1, y2 = y2, y1
                
    #     if x3 > x4:
    #         x3, x4 = x4, x3
    #     elif x3 == x4:
    #         if y3 > y4:
    #             y3, y4 = y4, y3

    #     if a2*b1-a1*b2:
    #         x = round((b2*c1-b1*c2)/(a2*b1-a1*b2),6)
    #         if max(x1,x3) <= x <= min(x2,x4):
    #             y = (-c1-a1*x)/b1 if b1 else (-c2-a2*x)/b2
    #             return [x,y]
    #         else:
    #             return []

    #     elif c1 == c2:
    #         if x1!=x2:
    #             for x in range(x1,x2+1):
    #                 if x3 <= x <= x4:
    #                     return [x,(-c1-a1*x)/b1]
    #             return []
            
    #         else:
    #             for y in range(y1,y2+1):
    #                 if y3 <= y <= y4:               
    #                     return [x1,y]
    #             return []
    #     else:
    #         return []
