class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        k = 0

        while candies > k*num_people*num_people + num_people*(num_people+1)//2:
            candies -= k*num_people*num_people + num_people*(num_people+1)//2
            k += 1
        
        res = [k*(k-1)*num_people//2+(i+1)*k for i in range(num_people)] if k else [0]*num_people

        index = 0
        while candies:
            if candies >= k*num_people + index + 1:
                candies -= k*num_people + index + 1
                res[index] += k*num_people + index + 1
                index += 1
            else:
                res[index] += candies
                break
            
        return res
