from collections import defaultdict, Counter
from typing import List


class SegmentTree:
  def __init__(self, n, op):
    self.N = n
    # op max -> -inf, min-> inf
    self.INF = float('-inf')
    self.SIZE = 1 << (n - 1).bit_length()
    self.data = [0] * (2 * self.SIZE)
    self.OP = op

  def __push_up(self, k):
    self.data[k] = self.OP(self.data[2 * k], self.data[2 * k + 1])

  def build(self, arr):
    for i in range(self.N):
      self.data[self.SIZE + i] = arr[i]
    for i in range(self.SIZE - 1, 0, -1):
      self.__push_up(i)

  def modify(self, p, x):
    p += self.SIZE
    self.data[p] = x
    p >>= 1
    while p >= 1:
      self.__push_up(p)
      p >>= 1

  def get(self, p):
    return self.data[p + self.SIZE]

  def query(self, l, r):
    # [l,r)
    if l >= r:
      return self.INF
    sml = smr = self.INF
    l += self.SIZE
    r += self.SIZE
    while l < r:
      if l & 1:
        sml = self.OP(sml, self.data[l])
        l += 1
      if r & 1:
        r -= 1
        smr = self.OP(self.data[r], smr)
      l >>= 1
      r >>= 1
    return self.OP(sml, smr)


class Solution:
  def maxRectangleArea(self, xCoord: List[int], yCoord: List[int]) -> int:
    d = {x: i for i, x in enumerate(sorted(set(yCoord)))}

    dic = defaultdict(list)
    for x, y in zip(xCoord, yCoord):
      dic[x].append(y)

    cnt = Counter()
    seg = SegmentTree(len(d) + 1, max)
    res = -1
    for x in sorted(dic):
      y = dic[x]
      y.sort()
      for i in range(len(y) - 1):
        if (y[i], y[i + 1]) in cnt:
          pre_x = cnt[(y[i], y[i + 1])]
          in_x = seg.query(d[y[i]], d[y[i + 1]] + 1)
          if in_x <= pre_x:
            res = max(res, (x - pre_x) * (y[i + 1] - y[i]))
        cnt[(y[i], y[i + 1])] = x

      for i in range(len(y)):
        seg.modify(d[y[i]], x)

    return res


s = Solution()
print(s.maxRectangleArea(xCoord=[1, 1, 3, 3], yCoord=[1, 3, 1, 3]))
