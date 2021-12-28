class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        letter = dict()
        res = -1
        for i, c in enumerate(s):
            if c not in letter:
                letter[c] = i
            else:
                res = max(res, i - letter[c] - 1)
        
        return res
