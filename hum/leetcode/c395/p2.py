from math import inf
from typing import List


class Solution:
  def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
    nums1.sort()
    nums2.sort()
    n = len(nums1)
    res = inf
    for i in range(n):
      for j in range(i + 1, n):
        s = set()
        x = inf
        idx = 0
        for k in range(n):
          if k == i or k == j: continue
          x = nums2[idx] - nums1[k]
          s.add(x)
          idx += 1
        if len(s) == 1:
          res = min(res, x)

    return res
