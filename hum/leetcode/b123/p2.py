from typing import List


class Solution:
  def numberOfPairs(self, points: List[List[int]]) -> int:
    n = len(points)
    points = sorted(points, key=lambda x: (x[0], -x[1]))
    inf = float('inf')
    res = 0
    for i in range(n):
      y = points[i][1]
      mid_y = -inf
      for j in range(i + 1, n):
        if points[j][1] <= y:
          if points[j][1] > mid_y:
            res += 1
          mid_y = max(points[j][1], mid_y)
    return res
