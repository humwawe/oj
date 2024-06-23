from math import inf
from typing import List


class Solution:
  def minimumSum(self, grid: List[List[int]]) -> int:
    return min(self.f(grid), self.f(self.rotate(grid)))

  def f(self, a: List[List[int]]) -> int:
    def minimumArea(a: List[List[int]], l: int, r: int) -> int:
      left, right = len(a[0]), 0
      top, bottom = len(a), 0
      for i, row in enumerate(a):
        for j, x in enumerate(row[l:r]):
          if x == 1:
            left = min(left, j)
            right = max(right, j)
            top = min(top, i)
            bottom = i
      return (right - left + 1) * (bottom - top + 1)

    res = inf
    m, n = len(a), len(a[0])
    if m >= 3:
      for i in range(1, m):
        for j in range(i + 1, m):
          area = minimumArea(a[:i], 0, n)
          area += minimumArea(a[i:j], 0, n)
          area += minimumArea(a[j:], 0, n)
          res = min(res, area)
    if m >= 2 and n >= 2:
      for i in range(1, m):
        for j in range(1, n):
          area = minimumArea(a[:i], 0, n)
          area += minimumArea(a[i:], 0, j)
          area += minimumArea(a[i:], j, n)
          res = min(res, area)

          area = minimumArea(a[:i], 0, j)
          area += minimumArea(a[:i], j, n)
          area += minimumArea(a[i:], 0, n)
          res = min(res, area)
    return res

  def rotate(self, a: List[List[int]]) -> List[List[int]]:
    return [col[::-1] for col in zip(*a)]
