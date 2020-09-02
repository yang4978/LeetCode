class Solution:
    def replaceSpace(self, s: str) -> str:
        i = 0
        l = len(s)
        while i < l:
            if s[i] == ' ':
                s = s[:i]+'%20'+s[i+1:]
                i += 2
                l += 2
            i += 1
        
        return s
