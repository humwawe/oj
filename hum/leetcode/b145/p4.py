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

  def is_same(self, x, y):
    return self.find(x) == self.find(y)

  def is_root(self, x):
    return self.p[x] < 0

  def count(self):
    cnt = 0
    for i in self.p:
      if i < 0:
        cnt += 1
    return cnt


class Solution:
  def countComponents(self, nums: List[int], threshold: int) -> int:
    dj = DJSet(threshold + 1)

    nums.sort()
    res = sum(1 if x > threshold else 0 for x in nums)
    n = len(nums)
    for x in nums:
      for j in range(x + x, threshold + 1, x):
        dj.merge(x, j)

    s = set()
    for x in nums:
      if x <= threshold:
        s.add(dj.find(x))

    return res + len(s)
