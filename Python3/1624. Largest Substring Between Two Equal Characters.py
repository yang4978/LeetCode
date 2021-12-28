class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letter = collections.defaultdict(list)
        for i, c in enumerate(s):
            letter[c].append(i)
        
        res = -1
        for arr in letter.values():
            res = max(res, arr[-1] - arr[0] - 1)
        
        return res
