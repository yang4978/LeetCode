class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp = set()
        res = set()
        for i in range(len(s)-9):
            if(s[i:i+10] not in temp):
                temp.add(s[i:i+10])
            else:
                res.add(s[i:i+10])
        return list(res)
        # res = []
        # str_dict = {}
        # for i in range(len(s)-10+1):
        #     if(s[i:i+10] in str_dict):
        #         str_dict[s[i:i+10]] += 1
        #     else:
        #         str_dict[s[i:i+10]] = 1
        # for s,num in str_dict.items():
        #     if(num>=2):
        #         res.append(s)
        # return res
