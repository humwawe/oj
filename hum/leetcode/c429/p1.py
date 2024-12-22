from typing import List


class Solution:
  def minimumOperations(self, nums: List[int]) -> int:
    cnt = 0
    while len(set(nums)) != len(nums):
      nums = nums[min(len(nums), 3):]
      cnt += 1
    return cnt
