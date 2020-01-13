class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        m = len(image)
        n = len(image[0])
        stack = [(sr,sc)]
        color = image[sr][sc]
        if color == newColor:
            return image
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while stack:
            x,y = stack.pop(0)
            image[x][y] = newColor
            for dx,dy in directions:
                if 0<=x+dx<m and 0<=y+dy<n and image[x+dx][y+dy] == color:
                    stack.append((x+dx,y+dy))
        
        return image
