from collections import deque
from math import inf
from typing import List


class Solution:
  def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
    n, m = len(grid), len(grid[0])
    a = [[-inf] * m for _ in range(n)]

    a[0][0] = health - grid[0][0]
    dq = deque()
    dq.append((0, 0))
    while dq:
      i, j = dq.popleft()
      for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        x, y = i + dx, j + dy
        if 0 <= x < n and 0 <= y < m and a[x][y] == -inf:
          a[x][y] = a[i][j] - grid[x][y]
          if grid[x][y] == 0:
            dq.appendleft((x, y))
          else:
            dq.append((x, y))
    return False if a[-1][-1] <= 0 else True
