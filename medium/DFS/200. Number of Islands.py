from typing import List

class Solution:
    def dfs(x, y, grid):
        grid[x][y] = "0"

        nx = [1, 0, -1, 0]
        ny = [0, 1, 0, -1]

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if dx >= 0 and dx < len(grid) and dy >= 0 and dy < len(grid[0]) and grid[dx][dy] == "1":
                Solution.dfs(dx, dy, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0

        r = len(grid)
        c = len(grid[0])

        for i in range(r):
            for k in range(c):
                if grid[i][k] == "1":
                    answer += 1
                    Solution.dfs(i, k, grid)

        return answer

answer = Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])

print("answer", answer)
