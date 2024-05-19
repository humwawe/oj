from itertools import pairwise
from typing import List


class Solution:
  def isArraySpecial(self, nums: List[int]) -> bool:
    for x, y in pairwise(nums):
      if x % 2 == y % 2:
        return False
    return True
