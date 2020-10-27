class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        num_dict = collections.defaultdict(int)

        for n in arr:
            num_dict[n] += 1

        return len(num_dict.values()) == len(set(num_dict.values()))
