import math
from typing import List


class Solution:
  def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:

    def check(mid):
      tmp = 0
      for wt in workerTimes:
        x = math.isqrt(mid * 2 // wt)
        t = 0
        for i in range(-10, 10, 1):
          u = x + i
          if u > 0:
            if u * (u + 1) // 2 * wt <= mid:
              t = u
        tmp += t
      return tmp >= mountainHeight

    l, r = 1, 10 ** 17
    while l < r:
      mid = l + r >> 1
      if check(mid):
        r = mid
      else:
        l = mid + 1
    return l
