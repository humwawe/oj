from collections import defaultdict
from typing import List


class Solution:
  def maxSelectedElements(self, nums: List[int]) -> int:
    nums.sort()
    n = len(nums)
    d = defaultdict(int)
    for i in range(n):
      d[nums[i] + 1] = d[nums[i]] + 1
      d[nums[i]] = d[nums[i] - 1] + 1

    return max(d.values())
