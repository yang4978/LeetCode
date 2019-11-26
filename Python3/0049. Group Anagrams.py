class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            letter = [0]*26
            for i in s:
                letter[ord(i)-ord('a')] += 1
            res[tuple(letter)].append(s)
        
        return res.values()
            
