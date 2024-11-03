from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
  def minTimeToReach(self, moveTime: List[List[int]]) -> int:
    n, m = len(moveTime), len(moveTime[0])
    dis = [[inf] * m for _ in range(n)]
    dis[0][0] = 0
    hpq = [(0, 0, 0)]

    while hpq:
      d, i, j = heappop(hpq)
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          continue
        if dis[nx][ny] > max(dis[i][j], moveTime[nx][ny]) + 1:
          dis[nx][ny] = max(dis[i][j], moveTime[nx][ny]) + 1
          heappush(hpq, (dis[nx][ny], nx, ny))

    return dis[n - 1][m - 1]
