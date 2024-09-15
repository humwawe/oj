from typing import List


class SegmentTree:
  def __init__(self, n, op):
    self.N = n
    self.INF = 0
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
  def maxPathLength(self, coordinates: List[List[int]], k: int) -> int:
    tx, ty = coordinates[k]
    coordinates.sort()
    tmp = set()
    for x, y in coordinates:
      tmp.add(x)
      tmp.add(y)
    d = {v: i for i, v in enumerate(sorted(tmp))}
    n = len(tmp)
    tx, ty = d[tx], d[ty]

    nd = {}
    for x, y in coordinates:
      nd.setdefault(d[x], []).append(d[y])

    seg = SegmentTree(n, max)
    pre = -1
    suf = -1
    for x in sorted(nd):
      ys = nd[x]
      ys.sort(reverse=True)
      for y in ys:
        cur = seg.query(0, y)
        if x == tx and y == ty:
          pre = cur

        seg.modify(y, max(cur + 1, seg.get(y)))
    seg = SegmentTree(n, max)
    for x in sorted(nd, reverse=True):
      ys = nd[x]
      ys.sort()
      for y in ys:
        cur = seg.query(y + 1, n)
        if x == tx and y == ty:
          suf = cur
        seg.modify(y, max(cur + 1, seg.get(y)))

    return pre + suf + 1


s = Solution()
print(s.maxPathLength(coordinates=[[2, 1], [5, 6]], k=1))
