class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:

        if x + y < z:
            return False
        
        if x == 0 or y == 0:
            return z == 0 or x + y == z

        return z % math.gcd(x,y) == 0

        # def transfer(b1,b2,w1,w2):
        #     if w1 + w2 <= b2:
        #         w1, w2 = 0, w1+w2
            
        #     if w1 + w2 > b2:
        #         w1, w2 = w1+w2-b2, b2

        #     return w1, w2

        # s = set()
        # queue = [(0,0)]

        # while queue:
        #     w1, w2 = queue.pop(0)
        #     if w1 + w2 == z:
        #         return True
        #     s |= {(w1,w2)}
        #     if (w1,0) not in s:
        #         queue.append((w1,0))
        #     if (w2,0) not in s:
        #         queue.append((w2,0))
        #     if (w1,y) not in s:
        #         queue.append((w1,y))
        #     if (x,w2) not in s:
        #         queue.append((x,w2))
            
        #     w1, w2 = transfer(x,y,w1,w2)
        #     if (w1,w2) not in s:
        #         queue.append((w1,w2))
        
        # return False
