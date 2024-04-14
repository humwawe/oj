from collections import defaultdict
from math import inf
from typing import List


class Solution:
  def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
    n, m = len(nums), len(andValues)
    dp = defaultdict(lambda: inf)
    dp[(0, -1)] = 0

    for num in nums:
      ndp = defaultdict(lambda: inf)
      for j, v in dp:
        if j < m and v & num >= andValues[j]:
          ndp[(j, v & num)] = min(ndp[(j, v & num)], dp[(j, v)])
        if j < m and v & num == andValues[j]:
          ndp[(j + 1, -1)] = min(ndp[(j + 1, -1)], dp[(j, v)] + num)
      dp = ndp

    return dp[(m, -1)] if dp[(m, -1)] < inf else -1
