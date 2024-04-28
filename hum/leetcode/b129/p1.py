from typing import List


class Solution:
  def canMakeSquare(self, grid: List[List[str]]) -> bool:
    n = 3

    def f(v):
      return 1 if v == 'B' else 0

    for i in range(n - 1):
      for j in range(n - 1):
        cnt = f(grid[i][j]) + f(grid[i + 1][j]) + f(grid[i][j + 1]) + f(grid[i + 1][j + 1])
        if cnt >= 3 or cnt <= 1:
          return True

    return False
