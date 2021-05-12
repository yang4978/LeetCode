class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xor = [0]
        for i in arr:
            xor.append(xor[-1] ^ i)

        res = []

        for start, end in queries:
            res.append(xor[end + 1] ^ xor[start])

        return res 
