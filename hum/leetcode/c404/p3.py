from typing import List


class Solution:
  def maximumLength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    res = 0
    for j in range(k):
      pos = [-1] * k
      dp = [0] * n
      pos[nums[0] % k] = 0
      dp[0] = 1
      for i in range(1, n):
        dp[i] = 1
        if pos[(j - nums[i]) % k] != -1:
          dp[i] = max(dp[i], dp[pos[(j - nums[i]) % k]] + 1)

        pos[nums[i] % k] = i

      res = max(res, max(dp))

    return res
