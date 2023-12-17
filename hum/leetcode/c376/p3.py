from bisect import bisect_left
from typing import List

pal = []
for i in range(10 ** 5):
  s = str(i)
  pal.append(int(s[:] + s[::-1]))
  pal.append(int(s[:-1] + s[::-1]))
pal.sort()
pal.append(10 ** 12 + 1)


class Solution:
  def minimumCost(self, nums: List[int]) -> int:
    n = len(nums)
    nums.sort()
    idx = bisect_left(pal, nums[(n - 1) // 2])
    return min(sum(abs(pal[idx] - i) for i in nums), sum(abs(pal[idx - 1] - i) for i in nums))
