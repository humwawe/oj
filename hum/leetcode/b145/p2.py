import itertools
from math import inf
from typing import List


class Solution:
  def findMinimumTime(self, strength: List[int], K: int) -> int:
    strength.sort()

    def f(arr, K):
      x = 1
      res = 0
      for v in arr:
        res += (v + x - 1) // x
        x += K

      return res

    res = inf
    for arr in itertools.permutations(strength):
      res = min(res, f(arr, K))
    return res
