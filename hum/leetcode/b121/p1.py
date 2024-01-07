from typing import List


class Solution:
  def missingInteger(self, nums: List[int]) -> int:
    n = len(nums)
    j = 0
    while j + 1 < n and nums[j + 1] - nums[j] == 1:
      j += 1

    se = set(nums)
    s = sum(nums[0:j + 1])
    while s in se:
      s += 1

    return s
