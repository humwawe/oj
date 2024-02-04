from itertools import accumulate
from typing import List


class Solution:
  def returnToBoundaryCount(self, nums: List[int]) -> int:
    cum = list(accumulate(nums))
    return cum.count(0)
