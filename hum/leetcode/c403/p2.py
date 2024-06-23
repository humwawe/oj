from typing import List


class Solution:
  def minimumArea(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    xl, xr = n, 0
    yl, yr = m, 0
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 1:
          xl = min(xl, i)
          xr = max(xr, i)
          yl = min(yl, j)
          yr = max(yr, j)
    return (xr - xl + 1) * (yr - yl + 1)
