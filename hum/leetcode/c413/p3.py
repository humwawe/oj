from functools import cache
from typing import List


class Solution:
  def maxScore(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    ans = 0
    ma = max(max(g) for g in grid)

    @cache
    def dfs(i, vis, acc):
      nonlocal ans
      if acc + ma * (n - i) <= ans:
        return
      if i == n:
        ans = max(ans, acc)
        return

      dfs(i + 1, vis, acc)
      for x in set(grid[i]):

        if (vis >> x) & 1 == 0:
          dfs(i + 1, vis | (1 << x), acc + x)

    dfs(0, 0, 0)
    return ans
