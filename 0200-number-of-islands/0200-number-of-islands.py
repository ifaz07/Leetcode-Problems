from collections import deque

class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    count += 1
                    q = deque([(r, c)])
                    grid[r][c] = "0"

                    while q:
                        x, y = q.popleft()

                        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                            nx, ny = x + dx, y + dy

                            if (0 <= nx < rows and
                                0 <= ny < cols and
                                grid[nx][ny] == "1"):
                                grid[nx][ny] = "0"
                                q.append((nx, ny))

        return count