from bisect import bisect_left
from typing import List


class Solution:
  def incremovableSubarrayCount(self, nums: List[int]) -> int:
    n = len(nums)
    j = n - 1
    for i in range(n - 2, -1, -1):
      if nums[i] < nums[i + 1]:
        j = i
      else:
        break

    stack = [0]
    res = 0
    for i in range(n):
      if i + 1 >= j:
        idx = bisect_left(stack, nums[i + 1] if i + 1 < n else 10 ** 11)
        res += idx
      if nums[i] > stack[-1]:
        stack.append(nums[i])
      else:
        stack.append(10 ** 12)
    return res
