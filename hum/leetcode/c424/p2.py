from typing import List


class Solution:
  def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
    n = len(nums)
    diff = [0] * (n + 1)

    for l, r in queries:
      diff[l] += 1
      diff[r + 1] -= 1
    for i in range(n):
      diff[i + 1] += diff[i]

    for i in range(n):
      if nums[i] > diff[i]:
        return False
    return True
