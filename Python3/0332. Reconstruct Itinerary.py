class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        route = collections.defaultdict(list)

        for i,j in tickets:
            route[i].append(j)
        
        for i in route:
            route[i].sort()

        ans = []

        def dfs(f):
            while route[f]:
                dfs(route[f].pop(0))
            ans.insert(0,f)
        
        dfs('JFK')
        return ans

        

        

