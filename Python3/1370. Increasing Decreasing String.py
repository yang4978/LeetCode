class Solution:
    def sortString(self, s: str) -> str:
        letter = collections.defaultdict(int)
        part = []
        for c in s:
            letter[c] += 1
            if len(part) < letter[c]:
                part.append([c])
            else:
                part[letter[c]-1].append(c)
        res = ""
        for i in range(len(part)):
            if i%2 == 0:
                res += ("").join(sorted(part[i]))
            else:
                res += ("").join(sorted(part[i],reverse=True))
        return res
