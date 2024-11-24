from functools import cache
from typing import List


class Solution:
  def minArraySum(self, nums: List[int], k: int, op1: int, op2: int) -> int:
    n = len(nums)
    a = [0] * n
    b = [0] * n
    c = [0] * n

    for i in range(n):
      a[i] = nums[i] // 2
      if nums[i] >= k:
        b[i] = k
        c[i] = k + (nums[i] - k) // 2
      if (nums[i] + 1) // 2 >= k:
        c[i] = max(c[i], nums[i] // 2 + k)

    @cache
    def dfs(i, op1, op2):
      if i == n:
        return 0
      t = dfs(i + 1, op1, op2)
      if op1 > 0:
        t = max(t, dfs(i + 1, op1 - 1, op2) + a[i])
      if op2 > 0:
        t = max(t, dfs(i + 1, op1, op2 - 1) + b[i])
      if op1 > 0 and op2 > 0:
        t = max(t, dfs(i + 1, op1 - 1, op2 - 1) + c[i])
      return t

    return sum(nums) - dfs(0, op1, op2)
