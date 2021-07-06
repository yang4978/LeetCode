class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        dishes = collections.defaultdict(list)
        table = set()
        for arr in orders:
            dishes[arr[2]].append(arr[1])
            table.add(int(arr[1]))
        
        res = [[0] * (1 + len(dishes)) for _ in range(1 + len(table))]

        res[0][0] = "Table"
        res[0][1:] = sorted(dishes.keys())

        i = 1
        table_order = dict()
        table = sorted(list(table))

        for t in table:
            res[i][0] = t
            table_order[str(t)] = i
            i += 1
        
        for i in range(1, len(res[0])):
            dish = res[0][i]
            for x in dishes[dish]:
                res[table_order[x]][i] += 1

        for i in range(1,len(res)):
            for j in range(len(res[0])):
                res[i][j] = str(res[i][j])

        return res
