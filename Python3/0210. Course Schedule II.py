class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        def dfs(course,index,used):
            
            if used[index] == -1:
                return True
            
            if used[index] == 1:
                return False
            
            used[index] = 1
            
            for j in course[index]:
                if dfs(course,j,used) == False:
                    return False
            
            used[index] = -1

            res.append(index)

            return True
        
        res = []
        course = collections.defaultdict(set)

        for i,j in prerequisites:
            course[i] |= {j}
        
        used = [0]*numCourses
        
        for i in range(numCourses):
            if dfs(course,i,used) == False:
                return []
        
        return res
