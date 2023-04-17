from collections import deque
from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if sr < 0 or sr >= len(image) or sc < 0 or sc >= len(image[0]):
            return None
        queue = deque([(sr, sc)])
        visited = set()
        start_color = image[sr][sc]
        image[sr][sc] = color
        while queue:
            sr, sc = queue.popleft()
            print(sr, sc)
            print(visited)
            if (sr, sc) in visited:
                continue
            for a, b in [(sr + 1, sc), (sr, sc - 1), (sr-1, sc), (sr, sc+1)]:
                if a >= 0 and a < len(image) and b >= 0 and b < len(image[0]):  
                    if image[a][b] == start_color:
                        image[a][b] = color
                        queue.append((a,b))
                        visited.add((a,b))

        return image