class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        set1 = set('qwertyuiopQWERTYUIOP')
        set2 = set('asdfghjklASDFGHJKL')
        set3 = set('zxcvbnmZXCVBNM')

        return [s for s in words if(set(s)<=set1 or set(s)<=set2 or set(s)<=set3)]
