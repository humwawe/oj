from typing import List


class Solution:
  def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    res = abs(nums[n // 2] - k)
    nums[n // 2] = k
    for i in range(n):
      if i <= n // 2:
        res += max(0, nums[i] - k)
      else:
        res += max(0, k - nums[i])
    return res
