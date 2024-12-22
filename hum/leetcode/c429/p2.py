from typing import List


class Solution:
  def maxDistinctElements(self, nums: List[int], k: int) -> int:
    n = len(nums)
    nums.sort()
    nums[0] = nums[0] - k
    for i in range(1, n):
      t = nums[i - 1] + 1
      if nums[i] - k <= t <= nums[i] + k:
        nums[i] = t
      elif nums[i] - k > t:
        nums[i] = nums[i] - k
      else:
        nums[i] = nums[i] + k
    return len(set(nums))
