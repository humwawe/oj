from typing import List


class NeighborSum:

  def __init__(self, grid: List[List[int]]):
    self.grid = grid
    self.n, self.m = len(grid), len(grid[0])
    self.pos = {}
    for i in range(self.n):
      for j in range(self.m):
        self.pos[grid[i][j]] = (i, j)

  def adjacentSum(self, value: int) -> int:
    x, y = self.pos[value]
    res = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < self.n and 0 <= ny < self.m:
        res += self.grid[nx][ny]
    return res

  def diagonalSum(self, value: int) -> int:
    x, y = self.pos[value]
    res = 0
    for dx, dy in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
      nx = x + dx
      ny = y + dy
      if 0 <= nx < self.n and 0 <= ny < self.m:
        res += self.grid[nx][ny]
    return res
