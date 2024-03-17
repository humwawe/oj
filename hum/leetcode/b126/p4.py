from typing import List


class Solution:
  def sumOfPower(self, nums: List[int], k: int) -> int:
    n = len(nums)
    dp = [[[0] * (k + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 1
    mod = 10 ** 9 + 7
    for i in range(1, n + 1):
      for j in range(n + 1):
        for l in range(k + 1):
          dp[i][j][l] += dp[i - 1][j][l]
          if j - 1 >= 0 and l - nums[i - 1] >= 0:
            dp[i][j][l] += dp[i - 1][j - 1][l - nums[i - 1]]
          dp[i][j][l] %= mod

    res = 0

    for j in range(n + 1):
      res = (res + dp[n][j][k] * pow(2, n - j, mod)) % mod

    return res
