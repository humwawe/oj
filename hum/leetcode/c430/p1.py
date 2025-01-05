from typing import List


class Solution:
  def minimumOperations(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    res = 0
    for j in range(m):
      for i in range(1, n):
        res += max(grid[i][j], grid[i - 1][j] + 1) - grid[i][j]
        grid[i][j] = max(grid[i][j], grid[i - 1][j] + 1)
    return res
