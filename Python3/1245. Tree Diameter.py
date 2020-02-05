class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        E = collections.defaultdict(list)

        for i,j in edges:
            E[i].append(j)
            E[j].append(i)
        
        l = len(E)

        used = [0]*l

        res = 0

        def dfs(index,used):
            nonlocal res
            max1 = 0
            max2 = 0
            used[index] = 1
            for i in E[index]:
                if not used[i]:
                    num = dfs(i,used)
                    if num>max1:
                        max2,max1 = max1,num
                    elif num>max2:
                        max2 = num
            
            res = max(res,max1+max2)

            return max(max1,max2)+1
        
        dfs(0,used)

        return res
