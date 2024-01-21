from typing import List

from sortedcontainers import SortedList


class Solution:
  def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
    left = SortedList()
    right = SortedList()
    n = len(nums)
    l = 1
    tot = 0
    res = float('inf')
    for r in range(1, n):
      right.add((nums[r], r))
      if len(right) + len(left) > dist + 1:
        t = (nums[l], l)
        if t in left:
          left.discard(t)
          tot -= t[0]
        right.discard(t)
        l += 1

      if len(right) > 0:
        t = right.pop(0)
        tot += t[0]
        left.add(t)

      while len(left) > k - 1:
        t = left.pop()
        tot -= t[0]
        right.add(t)

      if len(left) == k - 1:
        res = min(res, tot)

    return res + nums[0]
