class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        res = 0
        for t in range(1,len(set(s))+1):
            l = 0
            r = 0
            letter = collections.defaultdict(int)
            total_type = 0

            while r<len(s):
                letter[s[r]] += 1
                if(letter[s[r]]==1):
                    total_type += 1
                while total_type > t:       
                    letter[s[l]] -= 1
                    if letter[s[l]] == 0:
                        total_type -= 1
                        del letter[s[l]]
                    l += 1
                else:
                    if(min(letter.values())>=k):        
                        res = max(res,r-l+1)
                r += 1

        return res
