from typing import List


class Solution:
  def maximumPrimeDifference(self, nums: List[int]) -> int:
    l, r = -1, 0
    n = len(nums)

    def is_p(num):
      if num == 1:
        return False
      i = 2
      while i * i <= num:
        if num % i == 0:
          return False
        i += 1
      return True

    for i in range(n):
      if is_p(nums[i]):
        if l == -1:
          l = i
        r = i

    return r - l
