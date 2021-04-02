class Solution:
    def trap(self, height: List[int]) -> int:
        wall = [0]
        res = 0

        for h in height:
            if(h >= wall[0]):
                edge = min(h, wall[0])
                while(wall):
                    res += edge - wall.pop() 
            wall.append(h)

        rwall = [0]
        while(wall):
            h = wall.pop()
            if(h >= rwall[0]):
                edge = min(h, rwall[0])
                while(rwall):
                    res += edge - rwall.pop() 
            rwall.append(h)

        return res
