class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        n = num_people

        # k = 0

        # while candies > k*n*n + n*(n+1)//2:
        #     candies -= k*n*n + n*(n+1)//2
        #     k += 1

        k = int((-1/2 + math.sqrt(1/4+2*candies))/(n))

        candies -= k*(k-1)*n*n//2 + k*n*(n+1)//2
        
        res = [k*(k-1)*n//2+(i+1)*k for i in range(n)] if k else [0]*n

        for i in range(n):
            if candies >= k*n + i + 1:
                candies -= k*n + i + 1
                res[i] += k*n + i + 1
            else:
                res[i] += candies
                break
            
        return res

        # n = num_people

        # k = 0

        # while candies > k*n*n + n*(n+1)//2:
        #     candies -= k*n*n + n*(n+1)//2
        #     k += 1

        # index = 0
        # while candies:
        #     if candies >= k*n + index + 1:
        #         candies -= k*n + index + 1
        #         res[index] += k*n + index + 1
        #         index += 1
        #     else:
        #         res[index] += candies
        #         break
            
        # return res
