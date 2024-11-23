from heapq import heappush, heappop
from typing import List


class Solution:
  def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    qs = [[] for _ in range(n)]
    for l, r in queries:
      qs[l].append(r)

    diff = [0] * (n + 1)

    hpq = []

    cur = 0
    for i in range(n):
      cur += diff[i]

      for r in qs[i]:
        heappush(hpq, -r)

      while nums[i] - cur > 0:
        if not hpq or -hpq[0] < i:
          return -1
        t = -heappop(hpq)
        cur += 1
        diff[t + 1] -= 1

    return len(hpq)
