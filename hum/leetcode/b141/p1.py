from typing import List


class Solution:
  def minBitwiseArray(self, nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    for i in range(n):
      for x in range(nums[i]):
        if x | (x + 1) == nums[i]:
          res[i] = x
          break
    return res
