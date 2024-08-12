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
      self.p[x] += self.p[y]
      self.p[y] = x
    return x == y


class Solution:
  def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
    dj = DJSet(n - 1)
    cnt = n - 1

    res = []
    for a, b in queries:
      l = dj.find(a)
      r = dj.find(b - 1)
      while l < r:
        cnt -= 1
        dj.merge(r, l)
        l = dj.find(l + 1)

      res.append(cnt)
    return res
