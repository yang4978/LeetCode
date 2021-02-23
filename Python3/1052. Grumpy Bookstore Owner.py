class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        size = len(customers)
        temp = sum(customers[i] for i in range(size) if grumpy[i]==0)
        
        l = 0
        r = X-1
        temp += sum(customers[i] for i in range(X) if grumpy[i] == 1)
        res = temp

        while r<size-1:
            if grumpy[l] == 1:
                temp -= customers[l]
            l += 1
            r += 1
            if grumpy[r] == 1:
                temp += customers[r]
            res = max(res,temp)
        
        return res
