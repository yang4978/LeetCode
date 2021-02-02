class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        letter = collections.defaultdict(int)
        maxn = 0

        while j<len(s):
            letter[s[j]] += 1
            maxn = max(maxn,letter[s[j]])
            if j - i + 1 - maxn > k:
                letter[s[i]] -=1
                i += 1
            j += 1

        return j - i
        
