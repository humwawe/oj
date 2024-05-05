from math import inf
from typing import List


class Solution:
  def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
    mod = 10 ** 9 + 7
    n, mi, ma = len(nums), min(nums), max(nums)
    s = ma * n - sum(nums)
    if cost1 * 2 <= cost2:
      return s * cost1 % mod

    res = inf
    for x in range(ma, ma * 2 + 1):
      d = x - mi
      if d <= s - d:
        res = min(res, s // 2 * cost2 + s % 2 * cost1)
      else:
        res = min(res, (s - d) * cost2 + (d - (s - d)) * cost1)

      s += n

    return res % mod
