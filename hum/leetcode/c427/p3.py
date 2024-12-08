from itertools import accumulate
from math import inf
from typing import List


class Solution:
  def maxSubarraySum(self, nums: List[int], k: int) -> int:
    n = len(nums)
    acc = list(accumulate(nums, initial=0))
    res = -inf
    for i in range(0, k):
      tmp = acc[i]
      for j in range(i + k, n + 1, k):
        cur = acc[j]
        res = max(res, cur - tmp)
        tmp = min(tmp, acc[j])

    return res
