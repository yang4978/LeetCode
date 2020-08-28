class Solution:
    # 中心扩散法 #
    def shortestPalindrome(self, s: str) -> str:
        if(s==""):
            return s
        l = len(s)
        for i in range(l):
            temp = s[l-1:l-i-1:-1] + s
            l_temp = l+i

            if(temp[:l_temp//2]==temp[l_temp-1:l_temp//2-1:-1] or temp[:l_temp//2]==temp[l_temp-1:l_temp//2:-1]):
                return temp
    # 马拉车 #
    def shortestPalindrome(self, s: str) -> str:
        index = 0
        ss = '#'
        
        for c in s:
            ss += c + '#'
        
        R = 0
        C = 0

        l = len(s)
        p = [0]*(2*l+1)

        for i in range(2*l+1):
            mirror_i = 2*C - i
            if i + p[mirror_i] < R:
                p[i] = p[mirror_i]
            else:
                k = R - i + 1
                while i-k >= 0 and i+k < 2*l+1 and ss[i-k]==ss[i+k]:
                    k += 1
                p[i] = k-1
                C = i
                R = i + p[i]

            if C == p[C]:
                index = C

        return ''.join(reversed(list(s[index:])))+s
