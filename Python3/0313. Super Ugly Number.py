class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        stack = [1]
        l = len(primes)
        i_arr = [0]*l
        res_arr = primes[:]
        i = 1
        while i<n:
            min_val = min(res_arr)
            idx = res_arr.index(min_val)
            i_arr[idx] += 1
            
            if(min_val!=stack[-1]):
                stack.append(min_val)
                i += 1
            
            res_arr[idx] = stack[i_arr[idx]]*primes[idx]

        return stack[-1]
