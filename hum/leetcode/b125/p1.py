from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    nums.sort()
    n = len(nums)
    for i in range(n):
      if nums[i] >= k:
        return i

    return n
