class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        # card = collections.defaultdict(int)

        # for c in deck:
        #     card[c] += 1
        
        # arr = card.values()

        # d = list(set(arr))
        # x = d[0]

        # for i in d[1:]:
        #     x = math.gcd(x,i)
        
        # return True if x>1 else False

        from fractions import gcd
        vals = collections.Counter(deck).values()
        return reduce(gcd,vals)>1
