from math import gcd, lcm
from typing import List


class Solution:
  def maxLength(self, nums: List[int]) -> int:
    n = len(nums)
    res = 1
    for i in range(n):
      g = nums[i]
      l = nums[i]
      t = nums[i]
      for j in range(i + 1, n):
        g = gcd(g, nums[j])
        l = lcm(l, nums[j])
        t *= nums[j]
        if t == g * l:
          res = max(res, j - i + 1)
    return res