class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dicts = collections.defaultdict(int)

        for w in words:
            dicts[w] += 1
        
        arr = sorted(dicts.keys(), key = lambda x:(-dicts[x], x))

        return arr[:k]
