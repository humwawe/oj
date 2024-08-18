from itertools import accumulate
from typing import List


class Solution:
  def resultsArray(self, nums: List[int], k: int) -> List[int]:
    if k == 1:
      return nums
    diff = []
    n = len(nums)
    for i in range(1, n):
      if nums[i] - nums[i - 1] == 1:
        diff.append(1)
      else:
        diff.append(0)

    acc = list(accumulate(diff, initial=0))

    res = []
    for i in range(k - 1, n):
      if acc[i] - acc[i - (k - 1)] == k - 1:
        res.append(nums[i])
      else:
        res.append(-1)

    return res
