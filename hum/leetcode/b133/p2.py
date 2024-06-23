from typing import List


class Solution:
  def minOperations(self, nums: List[int]) -> int:
    n = len(nums)
    res = 0
    for i in range(n - 2):
      if nums[i] == 0:
        res += 1
        for j in range(3):
          nums[i + j] = 1 - nums[i + j]

    if nums[-1] == 0 or nums[-2] == 0:
      return -1
    return res
