from typing import List


class Solution:
  def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
    n = len(nums)
    for i in range(n):
      if i + 2 * k > n:
        break
      t1 = nums[i:i + k]
      t2 = nums[i + k:i + 2 * k]
      if t1 == sorted(t1) and t2 == sorted(t2) and len(set(t1)) == len(set(t2)) == k:
        return True
    return False
