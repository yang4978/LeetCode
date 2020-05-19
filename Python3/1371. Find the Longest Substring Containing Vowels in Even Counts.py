class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        pos = [-1]*(1<<5)
        pos[0] = 0
        status = 0
        ans = 0
        
        for i in range(len(s)):
            if s[i] == 'a':
                status ^= 1<<0
            elif s[i] == 'e':
                status ^= 1<<1
            elif s[i] == 'i':
                status ^= 1<<2
            elif s[i] == 'o':
                status ^= 1<<3
            elif s[i] == 'u':
                status ^= 1<<4
            
            if pos[status] == -1:
                pos[status] = i+1
            else:
                ans = max(ans,i+1-pos[status])

        return ans
