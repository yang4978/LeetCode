class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        pa = m - 1
        pb = n - 1
        pc = m + n - 1

        while pa>=0 and pb>=0:
            if A[pa] > B[pb]:
                A[pc] = A[pa]
                pa -= 1
            else:
                A[pc] = B[pb]
                pb -= 1
            pc -= 1

        while pb>=0:
            A[pc] = B[pb]
            pc -= 1
            pb -= 1
