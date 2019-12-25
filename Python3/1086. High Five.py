class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        note = {}

        for i,j in items:
            if i not in note:
                note[i] = [j]
            else:
                note[i].append(j)

        return [[i,sum(sorted(note[i])[-5:])//5]for i in sorted(note.keys())]
