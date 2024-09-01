from typing import List


class Solution:
  def maximumSubarrayXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
    n = len(nums)
    dp = [[0] * n for _ in range(n)]

    for i in range(n - 1, -1, -1):
      dp[i][i] = nums[i]
      for j in range(i + 1, n):
        dp[i][j] = dp[i][j - 1] ^ dp[i + 1][j]

    ma = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
      ma[i][i] = dp[i][i]
      for j in range(i + 1, n):
        ma[i][j] = max(dp[i][j], ma[i][j - 1], ma[i + 1][j])

    res = []
    for l, r in queries:
      res.append(ma[l][r])
    return res
