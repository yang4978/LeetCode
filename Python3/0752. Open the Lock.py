class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = [('0000',0)]

        deadends = set(deadends)

        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0

        while q:
            num, times = q.pop(0)
            for delta in [1, 9]:
                for i in range(4):
                    new_num = num[:i] + str((int(num[i]) + delta) % 10) + num[i + 1:]
                    if new_num == target:
                        return times + 1
                    if new_num not in deadends:
                        q.append((new_num, times + 1))
                        deadends.add(new_num)
                    
        return -1
