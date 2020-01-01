class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())
        # s += " "
        # res = 0
        # word = ""
        # for c in s:
        #     if c!=" ":
        #         word += c
        #     else:
        #         if word != "":
        #             res += 1
        #             word = ""
        
        # return res
