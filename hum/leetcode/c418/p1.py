from itertools import permutations
from typing import List


class Solution:
  def maxGoodNumber(self, nums: List[int]) -> int:
    res = 0
    for a, b, c in permutations(nums):
      res = max(res, int(bin(a)[2:] + bin(b)[2:] + bin(c)[2:], 2))
    return res
