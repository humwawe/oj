from itertools import pairwise
from typing import List


class Solution:
  def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
    tmp = [0]
    for x, y in pairwise(nums):
      if x % 2 != y % 2:
        tmp.append(tmp[-1] + 1)
      else:
        tmp.append(tmp[-1])

    res = []
    for l, r in queries:
      if r - l == tmp[r] - tmp[l]:
        res.append(True)
      else:
        res.append(False)
    return res
