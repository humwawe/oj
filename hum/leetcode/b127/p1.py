from typing import List


class Solution:
  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    n = len(nums)
    res = n + 1
    for i in range(n):
      cur = nums[i]
      for j in range(i, n):
        cur |= nums[j]
        if cur >= k:
          res = min(res, j - i + 1)
    if res == n + 1:
      return -1

    return res
