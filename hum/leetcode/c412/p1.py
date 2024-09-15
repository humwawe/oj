from typing import List


class Solution:
  def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
    for _ in range(k):
      i = nums.index(min(nums))
      nums[i] = nums[i] * multiplier

    return nums