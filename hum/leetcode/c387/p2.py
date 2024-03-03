from typing import List


class Solution:
  def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
    n, m = len(grid), len(grid[0])
    for i in range(n):
      for j in range(1, m):
        grid[i][j] += grid[i][j - 1]
    for j in range(m):
      for i in range(1, n):
        grid[i][j] += grid[i - 1][j]

    res = 0
    for i in range(n):
      for j in range(m):
        if grid[i][j] <= k:
          res += 1

    return res
