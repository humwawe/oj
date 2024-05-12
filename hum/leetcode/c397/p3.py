from math import inf
from typing import List


class Solution:
  def maxScore(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    dp = [[[0] * 2 for _ in range(m)] for _ in range(n)]

    res = -inf
    for i in range(n):
      for j in range(m):
        dp[i][j][0] = 0
        dp[i][j][1] = -inf
        if i - 1 >= 0:
          dp[i][j][1] = max(dp[i][j][1], max(dp[i - 1][j][0], dp[i - 1][j][1]) + grid[i][j] - grid[i - 1][j])
        if j - 1 >= 0:
          dp[i][j][1] = max(dp[i][j][1], max(dp[i][j - 1][0], dp[i][j - 1][1]) + grid[i][j] - grid[i][j - 1])

        res = max(res, dp[i][j][1])
    return res
