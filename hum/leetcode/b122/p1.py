from heapq import nsmallest
from typing import List


class Solution:
  def minimumCost(self, nums: List[int]) -> int:
    return nums[0] + sum(nsmallest(2, nums[1:]))
