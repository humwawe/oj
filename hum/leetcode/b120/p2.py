from typing import List


class Solution:
  def largestPerimeter(self, nums: List[int]) -> int:
    s = sum(nums)
    nums.sort()
    n = len(nums)
    for i in range(n - 1, 1, -1):
      if s - nums[i] > nums[i]:
        return s
      s -= nums[i]
    return -1
