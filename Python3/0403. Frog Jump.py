class Solution:
    def canCross(self, stones: List[int]) -> bool:
        l = len(stones)
        dp = defaultdict(set)
        set_stone = set(stones)
        dp[0] = {0}
        for s in stones:
            for step in dp[s]:
                for d in [-1, 0, 1]:
                    if step + d > 0 and (s + step + d) in set_stone:
                        dp[s+ + step + d].add(step + d)
        return len(dp[stones[-1]]) > 0
