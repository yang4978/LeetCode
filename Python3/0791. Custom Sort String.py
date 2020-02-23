class Solution:
    def customSortString(self, S: str, T: str) -> str:
        letter = {}
        
        l = len(S)

        for i in range(l):
            letter[S[i]] = i
        
        for i in range(ord('a'),ord('z')+1):
            if chr(i) not in letter:
                letter[chr(i)] = l
                l += 1
        
        arr = [0]*26

        for c in T:
            arr[letter[c]] += 1
        
        res = ""
        for i,c in enumerate(letter.keys()):
            res += c*arr[i]
        
        return res

        # letter = {}

        # for i in range(ord('a'),ord('z')+1):
        #     letter[chr(i)] = 26
        
        # for i in range(len(S)):
        #     letter[S[i]] = i
        
        # res = list(T)

        # res.sort(key = lambda x: letter[x])

        # return ''.join(res)
