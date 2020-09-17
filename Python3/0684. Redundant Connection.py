class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        def find(n,arr):
            while n!=arr[n]:
                n = arr[n]
            return n

        l = len(edges)
        arr = [i for i in range(l+1)]

        for x,y in edges:
            set1 = find(x,arr)
            set2 = find(y,arr)
            if set1 == set2:
                return [x,y]                
            else:
                arr[set1] = set2
        
        return []
