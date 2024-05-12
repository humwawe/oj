from typing import List


class Solution:
  def satisfiesConditions(self, grid: List[List[int]]) -> bool:
    n, m = len(grid), len(grid[0])
    for i in range(n):
      for j in range(m):
        if i + 1 < n:
          if grid[i][j] != grid[i + 1][j]:
            return False
        if j + 1 < m:
          if grid[i][j] == grid[i][j + 1]:
            return False

    return True
