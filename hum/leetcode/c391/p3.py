from typing import List


class Solution:
  def countAlternatingSubarrays(self, nums: List[int]) -> int:
    n = len(nums)
    l, r = 0, 0
    res = 0
    while l < n:
      while r + 1 < n and nums[r + 1] != nums[r]:
        r += 1
      length = (r - l + 1)
      res += length * (length + 1) // 2
      l, r = r + 1, r + 1

    return res
