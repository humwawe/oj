from typing import List


class FenwickTree:
  def __init__(self, n):
    self.N = n
    self.bit = [0] * n

  def set_bit(self, arr):
    self.bit = arr[:]

    for i in range(self.N):
      if i | (i + 1) < self.N:
        self.bit[i | (i + 1)] += self.bit[i]

  # [ ]
  def get_sum(self, l, r):
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
  def sumOfGoodSubsequences(self, nums: List[int]) -> int:
    n = len(nums)
    m = max(nums)
    fen = FenwickTree(m + 2)
    acc = FenwickTree(m + 2)
    fen.add(nums[0], 1)
    acc.add(nums[0], nums[0])
    res = nums[0]
    mod = 10 ** 9 + 7
    for i in range(1, n):
      cur_cnt = (fen.get_sum(nums[i] - 1, nums[i] - 1) + fen.get_sum(nums[i] + 1, nums[i] + 1) + 1) % mod
      pre_acc = acc.get_sum(nums[i] - 1, nums[i] - 1) + acc.get_sum(nums[i] + 1, nums[i] + 1)

      cur_acc = (pre_acc + cur_cnt * nums[i]) % mod

      res = (res + cur_acc) % mod
      fen.add(nums[i], cur_cnt)
      acc.add(nums[i], cur_acc)
    return res
