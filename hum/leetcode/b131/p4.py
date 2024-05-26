from typing import List

from sortedcontainers import SortedList


class SegmentTree:
  def __init__(self, n, op):
    self.N = n
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

  def all_prod(self):
    return self.data[1]


class Solution:
  def getResults(self, queries: List[List[int]]) -> List[bool]:
    n = max([x[1] for x in queries]) + 1
    sl = SortedList([0, n])
    seg = SegmentTree(n + 1, max)
    seg.build([0] * (n + 1))
    res = []
    for q in queries:
      x = q[1]
      i = sl.bisect_left(x)
      pre = sl[i - 1]
      if q[0] == 1:
        nex = sl[i]
        sl.add(x)
        seg.modify(x, x - pre)
        seg.modify(nex, nex - x)
      else:
        m = max(seg.query(0, pre + 1), x - pre)
        res.append(m >= q[2])

    return res
