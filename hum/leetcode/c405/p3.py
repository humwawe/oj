from typing import List


class Solution:
  def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    s1 = [[0] * (m + 1) for _ in range(n + 1)]
    s2 = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        s1[i][j] = s1[i - 1][j] + s1[i][j - 1] - s1[i - 1][j - 1] + (grid[i - 1][j - 1] == 'X')
        s2[i][j] = s2[i][j - 1] + s2[i - 1][j] - s2[i - 1][j - 1] + (grid[i - 1][j - 1] == 'Y')

    res = 0
    for i in range(1, n + 1):
      for j in range(1, m + 1):
        if s1[i][j] == s2[i][j] and s1[i][j] > 0:
          res += 1
    return res
