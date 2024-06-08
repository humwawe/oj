from typing import List


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

  def query(self, l, r):
    if l >= self.N:
      l = self.N - 1
    if r > self.N:
      r = self.N

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
  def findWinningPlayer(self, skills: List[int], k: int) -> int:
    n = len(skills)
    seg = SegmentTree(n, max)
    seg.build(skills)
    if seg.query(0, k + 1) == skills[0]:
      return 0

    for i in range(1, n):
      if seg.query(0, i + 1) == skills[i] and seg.query(i, i + k) == skills[i]:
        return i

    return -1
