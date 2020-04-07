class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:
        m = len(picture)
        if not m:
            return 0
        n = len(picture[0])

        row = collections.defaultdict(list)
        col = collections.defaultdict(list)

        for i in range(m):
            count = 0
            for j in range(n):
                if picture[i][j] == 'B':
                    col[j].append((i,j))
                    count += 1
                    p = (i,j)
            if count == 1:
                row[p[0]].append(p)

        s1 = set([col[i][0] for i in col if len(col[i])==1])
        s2 = set([row[i][0] for i in row])

        return len(s1&s2)
