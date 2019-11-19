class Solution:
    def nthUglyNumber(self, n: int) -> int:
        stack = [1] 
        i2 = i3 = i5 = 0
        for i in range(n-1):
            next2 = 2*stack[i2]
            next3 = 3*stack[i3]
            next5 = 5*stack[i5]

            min_next = min(next2,next3,next5)
            stack.append(min_next)
            
            if(next2==min_next): i2 += 1
            if(next3==min_next): i3 += 1
            if(next5==min_next): i5 += 1
        
        return stack[-1]
        # stack = [1]
        # i = 0
        # d = []
        # while(i<n):
        #     temp = min(stack)
        #     stack.remove(temp)
        #     if(2*temp not in stack):
        #         stack.append(2*temp)

        #     if(3*temp not in stack):
        #         stack.append(3*temp)

        #     if(5*temp not in stack):
        #         stack.append(5*temp)

        #     i += 1

        # return temp
