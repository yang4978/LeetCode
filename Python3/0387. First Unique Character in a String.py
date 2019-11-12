class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter = collections.defaultdict(int)
        
        for i in range(len(s)):
            letter[s[i]] += 1
        
        for i in range(len(s)):
            if letter[s[i]] == 1:
                return i
        return -1

        # letter = collections.defaultdict(list)
        
        # for i in range(len(s)):
        #     letter[s[i]] += [i]
        
        # num = [i[0] for i in letter.values() if len(i)==1]
        
        # if num==[]:
        #     return -1
        # else:
        #     return sorted(num)[0]
