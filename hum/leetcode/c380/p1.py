from collections import Counter
from typing import List


class Solution:
  def maxFrequencyElements(self, nums: List[int]) -> int:
    cnt = Counter(nums)
    v = max(cnt.values())
    res = 0
    for x in cnt.values():
      if v == x:
        res += x
    return res
