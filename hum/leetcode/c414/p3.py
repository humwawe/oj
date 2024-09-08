from typing import List


class Solution:
  def findMaximumScore(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [0] * n
    stack = []
    for i in range(n):
      if stack:
        dp[i] = dp[stack[-1]] + (i - stack[-1]) * nums[stack[-1]]
      if not stack or nums[i] > nums[stack[-1]]:
        stack.append(i)
    return dp[-1]
