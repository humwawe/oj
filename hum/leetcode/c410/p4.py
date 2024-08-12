from itertools import accumulate
from typing import List


class Solution:
  def countOfPairs(self, nums: List[int]) -> int:
    m = max(nums)
    n = len(nums)
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(nums[0] + 1):
      dp[0][i] = 1
    acc = list(accumulate(dp[0], initial=0))
    mod = 10 ** 9 + 7
    for i in range(1, n):
      for x in range(nums[i] + 1):
        y = nums[i] - x
        l, r = 0, min(nums[i - 1] - y, x)
        if r >= l:
          dp[i][x] = (acc[r + 1] - acc[l]) % mod
      acc = list(accumulate(dp[i], initial=0))

    return sum(dp[-1]) % mod
