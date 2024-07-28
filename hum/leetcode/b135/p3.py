from itertools import accumulate
from typing import List


class Solution:
  def minChanges(self, nums: List[int], k: int) -> int:
    n = len(nums)
    diff = [0] * (k + 2)
    for i in range(n // 2):
      x, y = nums[i], nums[n - i - 1]
      if x > y:
        x, y = y, x
      diff[0] += 2
      diff[k + 1] -= 2
      diff[0] += -1
      diff[max(k - x, y) + 1] -= -1
      diff[y - x] += -1
      diff[y - x + 1] -= -1

    s = list(accumulate(diff))
    return min(s[:-1])
