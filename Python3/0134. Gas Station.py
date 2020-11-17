class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0
        start = 0
        rest = 0
        station = 0
        l = len(gas)
        while station <= l:
            if rest>=0:
                i += 1
                rest += gas[i%l]-cost[i%l]
                station += 1
            else:
                start = i+1
                if start > l:
                    return -1
                rest = 0
                station = 0
        return i%l
