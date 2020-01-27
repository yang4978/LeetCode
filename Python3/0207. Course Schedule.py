class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        def dfs(course,index,used):           
            res = True

            for i in course[index]:
                if used[i] == 1:
                    return False
                else:
                    used[i] = 1
                    if dfs(course,i,used) == False:
                        return False
                    used[i] = 0
            
            return res

        course = collections.defaultdict(set)

        for i,j in prerequisites:
            course[i] |= {j}
        
        used = [0]*numCourses

        res = True
        for i in range(numCourses):
            if dfs(course,i,used) == False:
                return False

        return res
