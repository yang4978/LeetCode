class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        start = ""
        pos = 0
        temp = 0
        for arr in board:
            for c in arr:
                start += str(c)
                if c == 0:
                    pos = temp
                temp += 1
        if start == "123450":
            return 0        
        queue = [(start, pos)]

        used = set()
        used.add(start)

        move = [-1, 1, -3, 3]
        res = 0

        while queue:
            res += 1
            for _ in range(len(queue)):
                start, pos = queue.pop(0)
                for delta in move:
                    t_pos = pos + delta
                    if 0 <= t_pos <= 5 and abs(pos // 3 - t_pos // 3) == (abs(delta) // 3):
                        if delta < 0:
                            t_start = start[:t_pos] + start[pos] + start[t_pos + 1:pos] + start[t_pos] + start[pos + 1:]
                        else:
                            t_start =  start[:pos] + start[t_pos] + start[pos + 1:t_pos] + start[pos] + start[t_pos + 1:]
                        if t_start == "123450":
                            return res
                        elif t_start not in used:
                            used.add(t_start)
                            queue.append((t_start, t_pos))

        return -1
