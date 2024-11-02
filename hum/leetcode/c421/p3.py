from math import gcd
from typing import List


class Solution:
  def subsequencePairCount(self, nums: List[int]) -> int:
    n = len(nums)
    m = max(nums)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    mod = 10 ** 9 + 7
    for x in nums:
      ndp = [[0] * (m + 1) for _ in range(m + 1)]

      for j in range(m + 1):
        for k in range(m + 1):
          ndp[j][k] = (ndp[j][k] + dp[j][k]) % mod
          nj = gcd(j, x)
          nk = gcd(k, x)
          ndp[nj][k] = (ndp[nj][k] + dp[j][k]) % mod
          ndp[j][nk] = (ndp[j][nk] + dp[j][k]) % mod

      dp = ndp

    return sum(dp[i][i] for i in range(1, m + 1)) % mod
