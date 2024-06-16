from collections import Counter
from typing import List


class Solution:
  def maximumTotalDamage(self, power: List[int]) -> int:
    cnt = Counter(power)
    a = sorted(cnt.keys())
    m = len(a)
    dp = [0] * m
    for i in range(m):
      dp[i] = a[i] * cnt[a[i]]
      if i:
        dp[i] = max(dp[i], dp[i - 1])
      for j in range(3):
        if i - j - 1 >= 0 and a[i] - a[i - j - 1] > 2:
          dp[i] = max(dp[i], dp[i - j - 1] + a[i] * cnt[a[i]])
          break

    return dp[-1]
