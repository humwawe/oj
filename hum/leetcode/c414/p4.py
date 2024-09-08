from collections import deque
from functools import cache
from math import inf
from typing import List


class Solution:

  def maxMoves(self, kx: int, ky: int, positions: List[List[int]]) -> int:

    ps = [[kx, ky]] + positions
    n = len(ps)
    first = n % 2

    def f(x, y):
      return x * 50 + y

    def dis(sx, sy):
      dd = [-1] * 2500
      dd[f(sx, sy)] = 0
      que = deque()
      que.append((sx, sy))
      d8 = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
      while que:
        x, y = que.popleft()
        for i, j in d8:
          nx, ny = x + i, y + j
          if 0 <= nx < 50 and 0 <= ny < 50:
            if dd[f(nx, ny)] == -1:
              dd[f(nx, ny)] = dd[f(x, y)] + 1
              que.append((nx, ny))
      return dd

    dist = [[-1] * n for _ in range(n)]

    for i in range(n):
      d = dis(ps[i][0], ps[i][1])
      for j in range(n):
        dist[i][j] = d[f(ps[j][0], ps[j][1])]

    @cache
    def dfs(st, pos):
      if st == (1 << n) - 1:
        return 0
      turn = (n - st.bit_count() + 1) % 2
      if turn == first:
        t = 0
        for i in range(n):
          if (st >> i) & 1 == 0:
            t = max(t, dist[pos][i] + dfs(st | (1 << i), i))
      else:
        t = inf
        for i in range(n):
          if (st >> i) & 1 == 0:
            t = min(t, dist[pos][i] + dfs(st | (1 << i), i))

      return t

    return dfs(1, 0)
