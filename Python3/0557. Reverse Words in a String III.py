class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        res = ""
        for i in s:
            res+=" "+i[::-1]
        return res[1:]
