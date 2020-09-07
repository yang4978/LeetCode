class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
                Hash = {}
        for i in nums:
            Hash[i] = Hash.get(i, 0) + 1
        keyvalues = sorted(Hash.items(), key = lambda x: (x[1], x[0]), reverse=True)
        return [keyvalues[j][0] for j in range(k)]


        # occurence = collections.defaultdict(int)

        # for n in nums:
        #     occurence[n] += 1
        
        # occurence[float('inf')] = -1
        
        # res = [float('inf')]*k

        # for n in occurence:
        #     if occurence[n] < occurence[res[-1]]:
        #         continue
        #     else:
        #         index = k-1
        #         while index >= 0 and occurence[n] > occurence[res[index]]:
        #             index -= 1
        #         index += 1
        #         res.insert(index,n)
        #         res.pop()
        
        # return res
