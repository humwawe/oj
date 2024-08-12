from typing import List


class Solution:
  def countOfPairs(self, nums: List[int]) -> int:
    m = max(nums)
    n = len(nums)
    dp = [[0] * (m + 1) for _ in range(n)]
    for i in range(nums[0] + 1):
      dp[0][i] = 1
    mod = 10 ** 9 + 7
    for i in range(1, n):
      for x in range(nums[i] + 1):
        y = nums[i] - x
        for pre_x in range(x + 1):
          pre_y = nums[i - 1] - pre_x
          if pre_y >= y:
            dp[i][x] = (dp[i][x] + dp[i - 1][pre_x]) % mod

    return sum(dp[-1]) % mod
