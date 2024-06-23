from typing import List


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    res = 0
    for x in nums:
      t = x % 3
      res += min(t, 3 - t)
    return res
