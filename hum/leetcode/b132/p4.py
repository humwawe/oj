from collections import Counter
from typing import List


class Solution:
  def maximumLength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[0] * (k + 1) for _ in range(n)]
    res = 0
    for i in range(k + 1):
      cnt1 = Counter()

      m1, m2 = -1, -1
      for j in range(n):
        dp[j][i] = max(dp[j][i], cnt1[nums[j]] + 1)
        if m1 != -1 and i - 1 >= 0:
          if nums[j] != nums[m1]:
            dp[j][i] = max(dp[j][i], dp[m1][i - 1] + 1)
          else:
            if m2 != -1:
              dp[j][i] = max(dp[j][i], dp[m2][i - 1] + 1)

        cnt1[nums[j]] = dp[j][i]
        if i - 1 >= 0:
          if m1 == -1 or dp[j][i - 1] > dp[m1][i - 1]:
            m1, m2 = j, m1
          elif m2 == -1 or dp[j][i - 1] > dp[m2][i - 1]:
            m2 = j

    for i in range(n):
      for j in range(k + 1):
        res = max(res, dp[i][j])
    return res
