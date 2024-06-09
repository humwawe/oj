from typing import List


class Solution:
  def maxTotalReward(self, nums: List[int]) -> int:
    nums.sort()
    dp = 1
    for v in nums:
      x = dp & ((1 << v) - 1)
      dp |= x << v
    return dp.bit_length() - 1
