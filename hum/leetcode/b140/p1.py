from math import inf
from typing import List


class Solution:
  def minElement(self, nums: List[int]) -> int:
    res = inf
    for num in nums:
      cur = 0
      for c in str(num):
        cur += int(c)
      res = min(res, cur)
    return res
