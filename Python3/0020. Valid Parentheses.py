class Solution:
    def isValid(self, s: str) -> bool:
        
        pair = {'{':'}','[':']','(':')'}
        temp = ['?']
        
        for i in s:
            if(i in pair):
                temp.append(pair[i])
            else:
                if(temp.pop()!=i):
                    return False
        return len(temp)==1
        
        # while '{}' in s or '[]' in s or '()' in s :
        #     s = s.replace('{}','')
        #     s = s.replace('[]','')
        #     s = s.replace('()','')
        # return s == ''
