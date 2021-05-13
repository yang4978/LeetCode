class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        l = min(arrLen, steps//2 + 1)
        arr = [[0] * l for _ in range(2)]

        arr[0][0] = 1
        before = 0

        for _ in range(1, steps + 1):
            after = 1 - before
            for i in range(l):
                arr[after][i] = arr[before][i]
                if i - 1 >= 0:
                    arr[after][i] += arr[before][i - 1] 
                if i + 1 < l:
                   arr[after][i] += arr[before][i + 1]
            before = after
        return arr[after][0] % (10 ** 9 + 7)
