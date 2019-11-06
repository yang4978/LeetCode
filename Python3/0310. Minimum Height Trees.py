class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        node = collections.defaultdict(set)
        for i,j in edges:
            node[i] |= {j}
            node[j] |= {i}
        q = {i for i in node if len(node[i])==1}
        while(n>2):
            temp = set()
            for k in q:
                j = node[k].pop()
                node[j] -= {k}
                if(len(node[j])==1):
                    temp |= {j}
                n -= 1
            q = temp
        return list(q)
