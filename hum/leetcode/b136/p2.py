from typing import List


class Solution:
  def minFlips(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    t1 = 0
    for i in range(n):
      tmp = 0
      for j in range(m // 2):
        if grid[i][j] != grid[i][m - j - 1]:
          tmp += 1
      t1 += tmp

    t2 = 0
    for j in range(m):
      tmp = 0
      for i in range(n // 2):
        if grid[i][j] != grid[n - 1 - i][j]:
          tmp += 1
      t2 += tmp

    return min(t1, t2)
