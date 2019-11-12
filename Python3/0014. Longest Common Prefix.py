class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ""
        for i in zip(*strs):
            if len(set(i))==1:
                s += i[0]
            else:
                break
        return s
        # if strs == []:
        #     return ""
        # res = strs[0]
        # for s in strs[1:]:
        #     l = min(len(res),len(s))
        #     res = res[:l]
        #     for k in range(l):
        #         if res[k]!=s[k]:
        #             res = res[:k]
        #             break
            
        # return res
