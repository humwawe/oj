from math import inf
from typing import List


class Solution:
  def minimumOperations(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    cnt = [[0] * 10 for _ in range(m)]
    for i in range(n):
      for j in range(m):
        cnt[j][grid[i][j]] += 1

    dp = [n - cnt[0][i] for i in range(10)]

    for i in range(1, m):
      ndp = [inf] * 10
      for j in range(10):
        for k in range(10):
          if k != j:
            ndp[j] = min(ndp[j], dp[k] + n - cnt[i][j])
      dp = ndp

    return min(dp)
