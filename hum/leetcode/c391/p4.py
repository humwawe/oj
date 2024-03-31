from math import inf
from typing import List


class Solution:
  def minimumDistance(self, points: List[List[int]]) -> int:
    x, y = [], []
    for i, p in enumerate(points):
      x.append(((p[0] - p[1]), i))
      y.append(((p[0] + p[1]), i))
    x.sort()
    y.sort()

    res = inf
    for i, p in enumerate(points):
      t1, t2 = x[-1][0] - x[0][0], y[-1][0] - y[0][0]
      if i == x[0][1]:
        t1 = x[-1][0] - x[1][0]
      elif i == x[-1][1]:
        t1 = x[-2][0] - x[0][0]

      if i == y[0][1]:
        t2 = y[-1][0] - y[1][0]
      elif i == y[-1][1]:
        t2 = y[-2][0] - y[0][0]

      res = min(res, max(t1, t2))

    return res
