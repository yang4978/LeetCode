class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        id_map = collections.defaultdict(set)

        for i in range(len(pid)):
            id_map[ppid[i]] |= {pid[i]}
        
        i = 0
        l = 1
        res = [kill]
        while i<l:
            for n in id_map[res[i]]:
                res.append(n)
                l += 1
            i += 1

        return res
