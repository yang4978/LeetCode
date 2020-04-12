class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x1,y1,x2,y2 = *coordinates[0],*coordinates[1]

        if x1 - x2:
            k = (y1-y2)/(x1-x2)
            for p in coordinates[2:]:
                if (p[1]-y1)/(p[0]-x1) != k:
                    return False
        
        else:
            for p in coordinates[2:]:
                if p[0] != x1:
                    return False
        
        return True
