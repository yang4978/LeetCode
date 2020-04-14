class Solution:
    # def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
    #     direction = collections.defaultdict(set)

    #     for i,j in graph:
    #         direction[i].add(j)
        
    #     def dfs(start, target, used):
    #         if start == target:
    #             return True
    #         res = False
    #         for k in direction[start]:
    #             used[k] = 1
    #             res = res or dfs(k,target,used)
    #             used[k] = 0
    #         return res

    #     used = [0]*n

    #     return dfs(start,target,used)
        
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        # direction = collections.defaultdict(set)

        # for i,j in graph:
        #     direction[i].add(j)

        # used = [0]*n

        # queue = [start]

        # while queue:
        #     node = queue.pop(0)
        #     used[node] = 1
        #     for k in direction[node]:
        #         if k == target:
        #             return True

        #         if used[k] == 0:
        #             queue.append(k)
        
        # return False

        s = set([start])
        count = 1

        while 1:
            for i,j in graph:
                if i in s:
                    if j == target:
                        return True
                    s.add(j)
            if count == len(s):
                return False
            count = len(s)

        # s = set([start])
        # count = 1

        # while 1:
        #     for i,j in graph:
        #         if i in s:
        #             s.add(j)
        #     if count == len(s):
        #         break
        #     else:
        #         count = len(s)
        # return target in s
