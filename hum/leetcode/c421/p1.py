from math import gcd, lcm
from typing import List


class Solution:
  def maxScore(self, nums: List[int]) -> int:
    n = len(nums)

    def f(a, p):
      g, l = -1, -1
      for i in range(n):
        if i == p:
          continue
        if g == -1:
          g = nums[i]
          l = nums[i]
        else:
          g = gcd(g, nums[i])
          l = lcm(l, nums[i])
      return g * l

    res = 0
    for i in range(-1, n):
      res = max(res, f(nums, i))
    return res
