from typing import List


class Solution:
  def maxIncreasingSubarrays(self, nums: List[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(n - 2, -1, -1):
      if nums[i] < nums[i + 1]:
        dp[i] = dp[i + 1] + 1

    def check(mid):
      for i in range(n):
        if i + mid >= n:
          return False
        if dp[i] >= mid and dp[i + mid] >= mid:
          return True
      return False

    l, r = 1, n // 2
    while l < r:
      mid = l + r + 1 >> 1
      if check(mid):
        l = mid
      else:
        r = mid - 1
    return l
