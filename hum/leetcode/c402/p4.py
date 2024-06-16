from typing import List


class FenwickTree:
  def __init__(self, n):
    self.N = n
    self.bit = [0] * n

  def get_sum(self, l, r):
    if l > r:
      return 0
    return self.__get_sum(r) - self.__get_sum(l - 1)

  def __get_sum(self, r):
    res = 0
    while r >= 0:
      res += self.bit[r]
      r = (r & (r + 1)) - 1
    return res

  def add(self, idx, v):
    while idx < self.N:
      self.bit[idx] += v
      idx = idx | (idx + 1)

  def get(self, idx):
    return self.get_sum(idx, idx)

  def set(self, idx, v):
    self.add(idx, v - self.get(idx))


class Solution:
  def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    fen = FenwickTree(n)
    for i in range(1, n - 1):
      if nums[i - 1] < nums[i] > nums[i + 1]:
        fen.add(i, 1)
    res = []
    for t, a, b in queries:
      if t == 1:
        res.append(fen.get_sum(a + 1, b - 1))
      else:
        nums[a] = b
        for i in range(-1, 2):
          if a + i - 1 >= 0 and a + i + 1 <= n - 1 and nums[a + i - 1] < nums[a + i] > nums[a + i + 1]:
            fen.set(a + i, 1)
          else:
            if a + i >= 0 and a + i <= n - 1:
              fen.set(a + i, 0)
    return res
