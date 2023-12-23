from typing import List


class Solution:
  def incremovableSubarrayCount(self, nums: List[int]) -> int:
    res = 0
    n = len(nums)
    for i in range(n):
      for j in range(i + 1, n + 1):
        nm = nums[0:i] + nums[j: n]
        print(nm)
        if sorted(nm) == nm and len(set(nm)) == len(nm):
          res += 1
    return res
