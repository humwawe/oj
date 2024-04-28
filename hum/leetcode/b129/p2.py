from typing import List


class Solution:
  def numberOfRightTriangles(self, grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    row = [0] * n
    col = [0] * m
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 1:
          row[i] += 1
          col[j] += 1

    res = 0
    for i in range(n):
      for j in range(m):
        if grid[i][j] == 1:
          if row[i] > 1 and col[j] > 1:
            res += (row[i] - 1) * (col[j] - 1)

    return res
