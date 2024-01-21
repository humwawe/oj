from typing import List


class Solution:
  def canSortArray(self, nums: List[int]) -> bool:
    tmp = sorted(nums)
    n = len(nums)
    i, j = 0, 0
    res = []
    while i < n:
      j = i
      while j < n and nums[j].bit_count() == nums[i].bit_count():
        j += 1
      res.extend(sorted(nums[i:j]))
      i = j
    return tmp == res
