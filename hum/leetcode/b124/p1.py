from typing import List


class Solution:
  def maxOperations(self, nums: List[int]) -> int:
    n = len(nums)
    f = nums[0] + nums[1]
    res = 0
    for i in range(0, n - 1, 2):
      if nums[i] + nums[i + 1] == f:
        res += 1
      else:
        break
    return res
