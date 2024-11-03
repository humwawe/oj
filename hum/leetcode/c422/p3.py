from heapq import heappop, heappush
from math import inf
from typing import List


class Solution:
  def minTimeToReach(self, moveTime: List[List[int]]) -> int:
    n, m = len(moveTime), len(moveTime[0])
    dis = [[[inf] * 2 for _ in range(m)] for _ in range(n)]
    dis[0][0][0] = 0
    hpq = [(0, 0, 0, 0)]

    while hpq:
      d, i, j, k = heappop(hpq)
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx = i + dx
        ny = j + dy
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
          continue
        if k == 0:
          if dis[nx][ny][k ^ 1] > max(dis[i][j][k], moveTime[nx][ny]) + 1:
            dis[nx][ny][k ^ 1] = max(dis[i][j][k], moveTime[nx][ny]) + 1
            heappush(hpq, (dis[nx][ny][k ^ 1], nx, ny, k ^ 1))
        else:
          if dis[nx][ny][k ^ 1] > max(dis[i][j][k], moveTime[nx][ny]) + 2:
            dis[nx][ny][k ^ 1] = max(dis[i][j][k], moveTime[nx][ny]) + 2
            heappush(hpq, (dis[nx][ny][k ^ 1], nx, ny, k ^ 1))

    return min(dis[n - 1][m - 1])
