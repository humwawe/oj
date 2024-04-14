from math import lcm
from typing import List


class Solution:
  def findKthSmallest(self, coins: List[int], k: int) -> int:
    n = len(coins)
    l, r = 1, min(coins) * k

    d = [[] for _ in range(n + 1)]

    for i in range(1, 1 << n):
      lcm_res = 1
      for j in range(n):
        if i >> j & 1:
          lcm_res = lcm(lcm_res, coins[j])
      d[i.bit_count()].append(lcm_res)

    def check(v):
      res = 0
      for i, lis in enumerate(d):
        sign = 1 if i % 2 == 1 else -1
        for l in lis:
          res += sign * (v // l)
      return res

    while l < r:
      mid = l + r >> 1
      if check(mid) >= k:
        r = mid
      else:
        l = mid + 1

    return l
