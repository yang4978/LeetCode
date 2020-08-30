class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        used = [0]*n
        keys = [0]

        while keys:
            k = keys.pop()
            used[k] = 1

            for i in rooms[k]:
                if used[i] == 0:
                    keys.append(i)
        
        return sum(used) == n
