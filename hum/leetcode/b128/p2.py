from typing import List


class Solution:
  def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
    x = [x for x, y in points]
    x.sort()
    i = 0
    res = 0
    while i < len(x):
      j = i
      while j + 1 < len(x) and x[j + 1] - x[i] <= w:
        j += 1
      res += 1
      i = j + 1
    return res
