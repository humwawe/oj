from functools import cache
from typing import List


class Solution:
  def countPathsWithXorValue(self, grid: List[List[int]], k: int) -> int:
    n, m = len(grid), len(grid[0])

    mod = 10 ** 9 + 7

    @cache
    def dfs(x, y, num):
      if x == n - 1 and y == m - 1:
        if num == k:
          return 1
        else:
          return 0

      nx, ny = x + 1, y
      res = 0
      if nx < n:
        res += dfs(nx, ny, num ^ grid[nx][ny])
      nx, ny = x, y + 1
      if ny < m:
        res += dfs(nx, ny, num ^ grid[nx][ny])
      return res % mod

    return dfs(0, 0, grid[0][0])
