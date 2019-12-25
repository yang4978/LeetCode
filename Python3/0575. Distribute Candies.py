class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)),len(candies)//2)

        # typ = len(set(candies))
        # n = len(candies)

        # if typ>=n//2:
        #     return n//2
        # else:
        #     return typ
