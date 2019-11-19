class Solution:
    def numSquares(self, n: int) -> int:

        q = [(0,0)]
        seen = set()
        sq = [i**2 for i in range(int(n**0.5),0,-1)]

        while q:
            num,step = q.pop(0)
            for i in sq:
                if num+i == n:
                    return step+1
                elif num+i<n and num+i not in seen:
                    q.append((num+i,step+1))
                    seen.add(num+i)
        
        return 0

        # res = [i for i in range(n+1)]
        # sq = [i**2 for i in range(int(n**0.5)+1)]
        # for i in range(4,n+1):
        #     for j in range(int(i**0.5)//2,int(i**0.5)+1):
        #         res[i] = min(res[i],res[i-sq[j]]+1)

        # return res[-1]

        # from queue import Queue

        # q = Queue()
        # q.put((0,0))
        # seen = set()
        # sq = [i**2 for i in range(1,int(n**0.5)+1)]

        # while not q.empty():
        #     num,step = q.get()
        #     for i in sq:
        #         if num+i == n:
        #             return step+1
        #         elif num+i<n and (num+i,step+1) not in seen:
        #             q.put((num+i,step+1))
        #             seen.add((num+i,step+1))
        
        # return 0
