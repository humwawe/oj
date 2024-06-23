from typing import List


class Solution:
  def minimumAverage(self, nums: List[int]) -> float:
    n = len(nums)
    a = []
    nums.sort()
    for i in range(n // 2):
      a.append((nums[i] + nums[-1 - i]) / 2)
    return min(a)
