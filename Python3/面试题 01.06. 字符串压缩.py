class Solution:
    def compressString(self, S: str) -> str:
        l = len(S)

        if l<3:
            return S

        res = ""
        temp = S[0]
        count = 1

        for c in S[1:]:
            if c == temp:
                count += 1
            else:
                res += temp + str(count)
                count = 1
                temp = c
        res += temp + str(count)

        if len(res) >= l:
            return S
        else:
            return res
