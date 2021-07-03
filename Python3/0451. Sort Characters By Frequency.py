class Solution:
    def frequencySort(self, s: str) -> str:
        letter = collections.defaultdict(int)
        for c in s:
            letter[c] += 1
        
        res = ""

        for c in sorted(letter.keys(), key = lambda x : -letter[x]):
            res += c * letter[c]
        
        return res
