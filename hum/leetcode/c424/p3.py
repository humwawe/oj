from itertools import accumulate
from typing import List


class Solution:
  def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    n, m = len(nums), len(queries)
    queries.append([0, 0, 0])

    def check(mid):
      diff = [0] * (n + 1)
      for i in range(mid + 1):
        diff[queries[i][0]] += queries[i][2]
        diff[queries[i][1] + 1] -= queries[i][2]

      acc = list(accumulate(diff))
      for i in range(n):
        if nums[i] > acc[i]:
          return False
      return True

    l, r = -1, m
    while l < r:
      mid = l + r >> 1
      if check(mid):
        r = mid
      else:
        l = mid + 1

    if l == m:
      return -1
    else:
      return l + 1
