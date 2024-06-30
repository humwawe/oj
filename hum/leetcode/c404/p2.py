from typing import List


class Solution:
  def maximumLength(self, nums: List[int]) -> int:
    n = len(nums)

    def f(x):
      res = 0
      j = 0
      for i in range(n):
        if nums[i] % 2 == x[j % 2]:
          res += 1
          j += 1
      return res

    return max(f((0, 1)), f((0, 0)), f((1, 1)), f((1, 0)))
