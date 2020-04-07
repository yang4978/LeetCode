class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        num = collections.defaultdict(int)
        res = []
        
        for i in arr1:
            num[i] += 1

        for i in arr2:
            res += [i]*num[i]
            del num[i]

        for i in sorted(num.keys()):
            res += [i]*num[i]

        return res

        # l = len(arr2)
        # index = {}

        # for i in range(l):
        #     index[arr2[i]] = i
        
        # for i in arr1:
        #     if i not in index:
        #         index[i] = i + l
        
        # arr1.sort(key = lambda x:index[x])

        # return arr1
