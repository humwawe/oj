from math import inf
from typing import List


class Solution:
  def maximumTotalCost(self, nums: List[int]) -> int:

    n = len(nums)
    s = [0] * (n + 1)
    f = 1
    for i in range(n):
      s[i + 1] = s[i] + nums[i] * f
      f *= -1
    print(s)

    dp = [[0, 0] for _ in range(n + 1)]

    m0 = 0
    m1 = -inf
    for i in range(1, n + 1):
      dp[i][0] = m0 + s[i]
      dp[i][1] = m1 - s[i]

      if i % 2 == 0:
        m0 = max(m0, max(dp[i][0], dp[i][1]) - s[i])
      else:
        m1 = max(m1, max(dp[i][0], dp[i][1]) + s[i])

    return max(dp[n][0], dp[n][1])
