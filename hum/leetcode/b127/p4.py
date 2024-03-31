from collections import defaultdict
from math import inf
from typing import List


class Solution:
  def sumOfPowers(self, nums: List[int], k: int) -> int:
    n = len(nums)
    mod = 10 ** 9 + 7
    nums.sort()
    dp = defaultdict(int)
    dp[(inf, -inf, 0)] = 1
    for cur in nums:
      ndp = defaultdict(int)
      for st, v in dp.items():
        min_diff, pre_v, cnt = st
        ndp[st] += v
        n_st = (min(min_diff, cur - pre_v), cur, cnt + 1)
        if cnt + 1 <= k:
          ndp[n_st] += v
      dp = ndp

    res = 0
    for st, v in dp.items():
      min_diff, pre_v, cnt = st
      if cnt == k:
        res = (res + min_diff * v) % mod

    return res
