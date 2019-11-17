class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if(s==""):
            return s
        l = len(s)
        for i in range(l):
            temp = s[l-1:l-i-1:-1] + s
            l_temp = l+i

            if(temp[:l_temp//2]==temp[l_temp-1:l_temp//2-1:-1] or temp[:l_temp//2]==temp[l_temp-1:l_temp//2:-1]):
                return temp
