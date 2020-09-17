class UnionFind:
    def __init__(self,n):
        self.ancestor = list(range(n))
    
    def find(self,index):
        while index != self.ancestor[index]:
            index = self.ancestor[index]
        return index
    
    def union(self,index1,index2):
        self.ancestor[self.find(index2)] = self.find(index1)

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:

        l = len(edges)
        uf = UnionFind(l+1)
        parent = [i for i in range(l+1)]
        conflict = []
        cycle = []

        for x,y in edges:
            if parent[y] != y:
                conflict = [x,y]
            else:
                parent[y] = x
                if uf.find(x) == uf.find(y):
                    cycle = [x,y]
                else:
                    uf.union(x,y)
        
        if not conflict:
            return cycle
        else:
            if not cycle:
                return conflict
            else:
                return [parent[conflict[1]],conflict[1]]
