class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # Intuition: 
        # double for loop between m x n grid
        # store the indices that already have been visited -> set
        # store m, n length
        # CONDITION FOR 0:
        # -> if 0, continue onward
        # CONDITION FOR 1:
        # -> if 1, first store indices and then check nearest neighbor
        m, n, res = len(grid), len(grid[0]), 0
        visited = set()
        # helper function for recursive
        def neighbors(indices, visited):
            if indices in visited:
                return visited
            visited.add((indices[0], indices[1]))
            for y, x in [(1,0), (-1,0), (0,-1), (0,1)]: # top, bottom, left, right
                dy, dx = indices[0]+y, indices[1]+x
                if (dy, dx) in visited:
                    continue
                if dy < 0 or dy > m - 1 or dx < 0 or dx > n - 1:
                    continue
                if (dy, dx) not in visited and grid[dy][dx] != "0":
                    visited = neighbors((dy, dx), visited)
                else:
                    continue
            return visited
        for i in range(m):
            for j in range(n):
                land = grid[i][j]
                if land == "0":
                    continue
                elif (i, j) in visited:
                    continue
                else:
                    visited = neighbors((i,j), visited)
                    res += 1
        return res
    
if __name__ == "__main__":
    solution = Solution().numIslands
    assert(solution([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])==1)
    # Add your test cases here
    print("All test cases pass!")