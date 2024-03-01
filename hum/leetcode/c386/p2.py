from typing import List


class Solution:
  def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
    n = len(bottomLeft)

    def f(x1, x2, x3, x4):
      return max(0, min(x2, x4) - max(x1, x3))

    res = 0
    for i in range(n):
      for j in range(i):
        x = f(bottomLeft[i][0], topRight[i][0], bottomLeft[j][0], topRight[j][0])
        y = f(bottomLeft[i][1], topRight[i][1], bottomLeft[j][1], topRight[j][1])
        res = max(res, min(x, y) * min(x, y))

    return res
