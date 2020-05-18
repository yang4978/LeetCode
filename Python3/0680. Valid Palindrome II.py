class Solution:
    def validPalindrome(self, s: str) -> bool:
        s_rev = s[::-1]
        l = len(s)
        idx = -1
        for i in range(l):
            if s_rev[i] != s[i]:
                idx = i
                break
        
        if idx != -1:
            p1 = s[i:l-i-1]
            p2 = s[i+1:l-i]

            if p1 != p1[::-1] and p2 != p2[::-1]:
                return False
        
        return True
