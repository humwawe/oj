from itertools import combinations
from typing import List


class Solution:
  def hasTrailingZeros(self, nums: List[int]) -> bool:
    for x, y in combinations(nums, 2):
      if (x | y) & 1 == 0: return True
    return False
