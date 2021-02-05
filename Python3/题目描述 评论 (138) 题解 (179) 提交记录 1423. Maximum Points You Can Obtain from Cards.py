class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)-k
        res = sum(cardPoints[:n])
        l = 0
        min_res = res
        r = n-1
        while r < len(cardPoints)-1:
            res -= cardPoints[l]
            l += 1
            r += 1
            res += cardPoints[r]
            min_res = min(res,min_res)
        return sum(cardPoints) - min_res
