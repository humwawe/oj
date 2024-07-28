from typing import List


class DJSet:

  def __init__(self, n):
    self.p = [-1] * n

  def find(self, x):
    if self.p[x] < 0:
      return x
    nx = x
    while self.p[x] >= 0:
      x = self.p[x]
    while nx != x:
      self.p[nx], nx = x, self.p[nx]
    return x

  def merge(self, x, y):
    x = self.find(x)
    y = self.find(y)
    if x != y:
      if self.p[y] < self.p[x]:
        x, y = y, x
      self.p[x] += self.p[y]
      self.p[y] = x
    return x == y


class Solution:
  def canReachCorner(self, X: int, Y: int, circles: List[List[int]]) -> bool:
    n = len(circles)
    dj = DJSet(n + 2)
    for i in range(n):
      x, y, r = circles[i]
      if x <= r or y + r >= Y:
        dj.merge(i, n)
      if y <= r or x + r >= X:
        dj.merge(i, n + 1)
      for j in range(i):
        x1, y1, r1 = circles[j]
        if (x - x1) ** 2 + (y - y1) ** 2 <= (r - r1) ** 2:
          dj.merge(i, j)

    if dj.find(n) == dj.find(n + 1):
      return False
    return True
