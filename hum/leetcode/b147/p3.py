from typing import List


class Solution:
  def longestSubsequence(self, nums: List[int]) -> int:
    m = max(nums)
    dp = [[0] * m for _ in range(m + 1)]
    suf_max = [[0] * (m + 1) for _ in range(m + 1)]
    for v in nums:
      for pre in range(1, m + 1):
        d = abs(v - pre)
        dp[v][d] = max(dp[v][d], suf_max[pre][d] + 1)
      for i in range(m - 1, -1, -1):
        suf_max[v][i] = max(suf_max[v][i + 1], dp[v][i])
    return max(max(x) for x in dp)