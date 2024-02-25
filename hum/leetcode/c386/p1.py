from collections import Counter
from typing import List


class Solution:
  def isPossibleToSplit(self, nums: List[int]) -> bool:
    cnt = Counter(nums)
    if max(cnt.values()) >= 3:
      return False
    else:
      return True
