class Solution:
    def toGoatLatin(self, S: str) -> str:
        vowel = {'a','e','i','o','u','A','E','I','O','U'}
        res = ''

        for i,word in enumerate(S.split(' ')):
            if word[0] in vowel:
                res += word 
            else:
                res += word[1:] + word[0]
            
            res += 'ma' + (i+1)*'a' + ' '
        
        return res[:-1]
