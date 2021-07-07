class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        mod = 10 ** 9 + 7
        res = 0
        meals = collections.defaultdict(int)
        max_num = max(deliciousness) * 2

        for d in deliciousness:
            exp = 1
            while exp <= max_num:
                if exp - d in meals:
                    res = (res + meals[exp - d]) % mod
                exp *= 2
            meals[d] += 1
        
        return res
