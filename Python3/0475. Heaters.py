class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        res = []
        houses.sort()
        heaters.sort()
        l = len(heaters)
        left = 0

        for c in houses:
            right = l-1
            while left<right:
                mid = (left+right)//2
                if heaters[mid]<c:
                    left = mid + 1
                else:
                    right = mid

            res.append(min(abs(c-heaters[left]),abs(heaters[left-1]-c)))
    
        return max(res)
