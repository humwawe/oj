from functools import cache
from typing import List


class Solution:
  def maxOperations(self, nums: List[int]) -> int:
    n = len(nums)

    @cache
    def f(s, t, v):
      if s >= t:
        return 0
      res = 0
      if nums[s] + nums[t] == v:
        res = max(res, f(s + 1, t - 1, v) + 1)
      if nums[s] + nums[s + 1] == v:
        res = max(res, f(s + 2, t, v) + 1)
      if nums[t] + nums[t - 1] == v:
        res = max(res, f(s, t - 2, v) + 1)
      return res

    return max(f(1, n - 2, nums[0] + nums[-1]), f(2, n - 1, nums[0] + nums[1]), f(0, n - 3, nums[-1] + nums[-2])) + 1
