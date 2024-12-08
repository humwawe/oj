from typing import List


class Solution:
  def minOperations(self, nums: List[int], k: int) -> int:
    s = set()
    for x in nums:
      if x < k:
        return -1
      s.add(x)

    res = len(s) - 1
    if min(s) > k:
      res += 1
    return res
