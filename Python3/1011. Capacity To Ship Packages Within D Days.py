class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        l = len(weights)
        # arr = [0] * (l + 1)
        # for i in range(1, 1 + l):
        #     arr[i] = arr[i - 1] + weights[i - 1]


        def canShip(cap):
            init = 0
            day = 1
            for n in weights:
                if init + n > cap:
                    init = n
                    day += 1
                    if day > D:
                        return False
                else:
                    init += n
            return True
            # init = 0
            # i = 0
            # for _ in range(D):
            #     i = bisect.bisect_right(arr, init + cap) - 1
            #     init = arr[i]
            # return i == l

        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2
            if(canShip(mid)):
                right = mid
            else:
                left = mid + 1
        
        return left
            
