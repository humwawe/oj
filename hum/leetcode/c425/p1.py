from typing import List


class Solution:
  def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    tmp = 10 ** 10
    n = len(nums)
    for length in range(l, r + 1):
      for i in range(n):
        if i + length > n:
          break
        t = sum(nums[i:i + length])
        if t > 0:
          tmp = min(tmp, t)

    if tmp == 10 ** 10:
      return -1
    return tmp
