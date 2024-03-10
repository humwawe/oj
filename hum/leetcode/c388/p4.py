from typing import List


class Solution:
  def maximumStrength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    inf = float('inf')
    dp = [[-inf] * (k + 1) for _ in range(n)]
    dp[0][1] = nums[0] * k
    for i in range(n):
      dp[i][0] = 0
    for i in range(1, n):
      for j in range(1, k + 1):
        if j % 2 == 0:
          dp[i][j] = max(dp[i - 1][j - 1] - nums[i] * (k - j + 1), dp[i - 1][j] - nums[i] * (k - j + 1))
        else:
          dp[i][j] = max(dp[i - 1][j - 1] + nums[i] * (k - j + 1), dp[i - 1][j] + nums[i] * (k - j + 1))

    return max(dp[i][k] for i in range(n))
