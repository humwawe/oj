from math import inf
from typing import List


class Solution:
  def maxSubarraySum(self, nums: List[int]) -> int:
    n = len(nums)
    f = -inf
    s = 0
    last = {}

    def update(x: int) -> int:
      nonlocal f, s
      res = f  # f[i-1]
      f = max(f, 0) + x  # f[i] = max(f[i-1], 0) + x
      if x in last:
        res = max(res, last[x] + s)  # s[i]
      s += x  # s[i+1] = s[i] + x
      last[x] = res - s
      return res

    suf = [0] * n
    for i in range(n - 1, -1, -1):
      suf[i] = update(nums[i])

    ans = f = -inf
    s = 0
    last = {}
    for x, sf in zip(nums, suf):
      pre = update(x)
      ans = max(ans, f, pre + sf, pre, sf)
    return ans
