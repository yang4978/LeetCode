class Solution:
    def numWays(self, n: int, relation: List[List[int]], k: int) -> int:
        num = collections.defaultdict(list)
        res = collections.defaultdict(int)
        for x,y in relation:
            num[x].append(y)

        res[0] = 1
        for _ in range(k):
            temp = collections.defaultdict(int)
            for i in res:
                for j in num[i]:
                    temp[j] += res[i]

            res = temp
        
        return res[n-1]
