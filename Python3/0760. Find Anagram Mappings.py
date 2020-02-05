class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        num = collections.defaultdict(list)

        for i,b in enumerate(B):
            num[b].append(i)
        
        return [num[i].pop() for i in A]
