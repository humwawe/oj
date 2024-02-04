from itertools import accumulate
from typing import List


class Solution:
  def maximumSubarraySum(self, nums: List[int], k: int) -> int:
    cum = list(accumulate(nums, initial=0))
    n = len(nums)
    d = dict()
    inf = float('inf')
    res = -inf
    for i in range(n):
      need = nums[i] - k
      res = max(res, cum[i + 1] - d.get(need, inf))
      need = nums[i] + k
      res = max(res, cum[i + 1] - d.get(need, inf))
      d[nums[i]] = min(d.get(nums[i], inf), cum[i])

    return res if res != -inf else 0
