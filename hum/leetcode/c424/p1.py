from typing import List


class Solution:
  def countValidSelections(self, nums: List[int]) -> int:
    n = len(nums)
    s = sum(nums)
    t = 0
    res = 0
    for i in range(n):
      if nums[i] == 0:
        if t == s:
          res += 2
        elif abs(t - s) == 1:
          res += 1
      t += nums[i]
      s -= nums[i]

    return res
