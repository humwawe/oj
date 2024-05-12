from math import inf
from typing import List


class Solution:
  def maximumEnergy(self, energy: List[int], k: int) -> int:
    n = len(energy)
    dp = energy[:]
    res = -inf
    for i in range(n):
      if i - k >= 0:
        dp[i] = max(dp[i], dp[i - k] + energy[i])
      if i + k >= n:
        res = max(res, dp[i])
    return res
