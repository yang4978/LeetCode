class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        res = 0
        temp = sum(calories[:k])

        if temp > upper:
            res += 1
        elif temp < lower:
            res -= 1

        for i in range(k,len(calories)):
            temp = temp - calories[i-k] + calories[i]

            if temp > upper:
                res += 1
            elif temp < lower:
                res -= 1
        
        return res
