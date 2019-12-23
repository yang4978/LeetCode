class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            flag = 1
            while stack and stack[-1]>0 and i<0:
                if stack[-1]+i<0:
                    stack.pop()
                elif stack[-1]+i>0:
                    flag = 0
                    break
                else:
                    stack.pop()
                    flag = 0
                    break
            if flag:
                stack.append(i)
        
        return stack
                

        # collision = 1
        # l = len(asteroids)
        # while collision:
        #     i = 0
        #     collision = 0
        #     while i<l-1:
        #         while i<l-1 and asteroids[i]>=0 and asteroids[i+1]<=0:
        #             collision = 1
        #             if asteroids[i]+asteroids[i+1]<0:
        #                 asteroids.pop(i)
        #             elif asteroids[i]+asteroids[i+1]>0:
        #                 asteroids.pop(i+1)
        #             else:
        #                 asteroids.pop(i)
        #                 asteroids.pop(i)
        #                 l -= 1
        #             l -= 1
        #         i += 1
        # return asteroids
