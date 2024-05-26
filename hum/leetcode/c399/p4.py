from typing import List


class SegmentTree:
  def __init__(self, n):
    self.N = n
    self.INF = float('-inf')
    self.SIZE = 1 << (n - 1).bit_length()
    self.data = [(0, 0, 0, 0)] * (2 * self.SIZE)

  def __push_up(self, k):
    self.data[k] = self.OP(self.data[2 * k], self.data[2 * k + 1])

  def OP(self, x, y):
    x1, y1, z1, d1 = x
    x2, y2, z2, d2 = y
    return (max(x1 + x2, z1 + d2), max(y1 + y2, d1 + z2), max(x1 + z2, z1 + y2), max(y1 + d2, d1 + x2))

  def build(self, arr):
    for i in range(self.N):
      self.data[self.SIZE + i] = (0, 0, 0, max(arr[i], 0))
    for i in range(self.SIZE - 1, 0, -1):
      self.__push_up(i)

  def modify(self, p, x):
    p += self.SIZE
    self.data[p] = (0, 0, 0, max(x, 0))
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
  def maximumSumSubsequence(self, nums: List[int], queries: List[List[int]]) -> int:
    mod = 10 ** 9 + 7
    n = len(nums)
    seg = SegmentTree(n)
    seg.build(nums)
    res = 0
    for x, y in queries:
      seg.modify(x, y)
      res = (res + seg.all_prod()[3]) % mod
    return res
