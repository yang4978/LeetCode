class Solution:
    def pourWater(self, heights: List[int], V: int, K: int) -> List[int]:
        n = len(heights)
    
        while V:
            t = V
            for d in (-1,1):
                i = best = K
                while 0<=i+d<len(heights) and heights[i+d]<=heights[i]:
                    if heights[i+d]<heights[i]:
                        best = i+d
                    i += d
                if best!=K:
                    heights[best] += 1
                    V -= 1
                    break

            #if(t==V):
            else:
                heights[K] += 1
                V -= 1

        return heights
                    
